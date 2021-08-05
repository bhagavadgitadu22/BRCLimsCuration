CREATE EXTENSION IF NOT EXISTS pg_trgm;

DROP TABLE IF EXISTS faux_genus;
DROP TABLE IF EXISTS vrai_genus;
DROP TABLE IF EXISTS grp_a_changer;

SELECT genus.don_lib
INTO TEMPORARY TABLE faux_genus
FROM t_donneedico AS genus
LEFT JOIN taxonomy
ON genus.don_lib = taxonomy.genus_name
WHERE taxonomy.genus_name IS NULL
AND genus.don_dic_id = 3755
AND genus.don_parent = 0
AND genus.don_lib NOT LIKE '% %'
ORDER BY genus.don_lib;

SELECT DISTINCT genus_name
INTO TEMPORARY TABLE vrai_genus
FROM taxonomy;

WITH grp AS (
	SELECT don_lib AS mistake, genus_name as correction, 
	SIMILARITY(genus_name, don_lib) AS distance,
	RANK() OVER (PARTITION BY don_lib ORDER BY SIMILARITY(genus_name, don_lib) DESC) AS rn
	FROM faux_genus, vrai_genus
) 
SELECT mistake, correction, distance 
INTO TEMPORARY TABLE grp_a_changer
FROM grp
WHERE rn = 1 AND distance > 0.5
ORDER BY distance;

UPDATE t_donneedico
SET don_lib = correction
FROM grp_a_changer
WHERE don_lib = mistake;