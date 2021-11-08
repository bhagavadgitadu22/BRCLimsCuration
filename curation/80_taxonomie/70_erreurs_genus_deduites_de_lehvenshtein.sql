CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

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
AND genus.xxx_sup_dat IS NULL
ORDER BY genus.don_lib;

SELECT DISTINCT genus_name
INTO TEMPORARY TABLE vrai_genus
FROM taxonomy;

WITH grp AS (
	SELECT don_lib AS mistake, genus_name as correction, 
	levenshtein_less_equal(genus_name, don_lib, 3) AS distance,
	RANK() OVER (PARTITION BY don_lib ORDER BY levenshtein_less_equal(genus_name, don_lib, 3)) AS rn
	FROM faux_genus, vrai_genus
) 
SELECT mistake, correction, distance 
INTO TEMPORARY TABLE erreurs_genus
FROM grp
WHERE rn = 1 AND distance <= 2
ORDER BY distance, mistake, correction;

UPDATE t_donneedico
SET don_lib = correction
FROM erreurs_genus
WHERE don_lib = mistake
AND mistake IN (
'Anerofustis',
'Anoxybacilllus',
'Aquaspirullum',
'Artrobacter',
'Branchybacterium',
'Edwarsiella',
'Heptococcus',
'Indicoccus',
'Lactobacilus',
'Micromonosopora',
'Oceanibacillus',
'Pseudoaeromonas',
'Pseudoarcicella',
'Rubromonas',
'Shingomonas',
'Acidiminas',
'Acidovorans',
'Natrionella',
'Ochrobacterium',
'Pseudosphingobacteri'
)
AND t_donneedico.don_dic_id = 3755
AND t_donneedico.xxx_sup_dat IS NULL;

DROP TABLE IF EXISTS faux_genus;
DROP TABLE IF EXISTS vrai_genus;
DROP TABLE IF EXISTS grp_a_changer;
