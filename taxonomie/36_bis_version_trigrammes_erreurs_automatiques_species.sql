CREATE EXTENSION IF NOT EXISTS pg_trgm;

DROP TABLE IF EXISTS faux_species;
DROP TABLE IF EXISTS grp_a_changer;

SELECT genus.don_lib AS genus, species.don_lib AS species
INTO TEMPORARY TABLE faux_species
FROM t_donneedico AS species
JOIN t_donneedico AS genus
ON species.don_parent = genus.don_code
WHERE genus.don_dic_id = 3755
AND genus.don_parent = 0
AND species.don_dic_id = 3755
AND (genus.don_lib, species.don_lib) NOT IN (SELECT genus_name, sp_epithet FROM taxonomy)
ORDER BY species.don_lib;

WITH grp AS (
	SELECT genus, species, genus_name, sp_epithet,
	SIMILARITY(
		CONCAT(genus_name, ' ', sp_epithet), 
		CONCAT(genus, ' ', species)
	) AS distance,
	RANK() OVER (PARTITION BY genus, species ORDER BY SIMILARITY(CONCAT(genus_name, ' ', sp_epithet), CONCAT(genus, ' ', species)) DESC) AS rn
	FROM faux_species, taxonomy
) 
SELECT genus, species, genus_name, sp_epithet, distance 
FROM grp
WHERE rn = 1 AND distance > 0.5
ORDER BY distance;
