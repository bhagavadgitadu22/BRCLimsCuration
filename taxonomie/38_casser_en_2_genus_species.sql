DROP TABLE IF EXISTS ids_genus_species;

SELECT genus_species.xxx_id, genus.don_code AS new_don_parent
INTO TEMPORARY TABLE ids_genus_species
FROM t_donneedico AS genus
JOIN t_donneedico AS genus_species
ON LOWER(genus.don_lib) = SPLIT_PART(LOWER(genus_species.don_lib), ' ', 1)
WHERE genus.don_dic_id = 3755 
AND genus.don_dic_id = genus_species.don_dic_id
AND genus.don_parent = 0
AND genus_species.don_parent = 0
AND LOWER(genus_species.don_lib) 
IN (SELECT CONCAT(LOWER(genus_name), ' ', LOWER(sp_epithet)) FROM taxonomy);

UPDATE t_donneedico
SET don_parent = ids_genus_species.new_don_parent,
don_lib = SPLIT_PART(don_lib, ' ', 2)
FROM ids_genus_species
WHERE t_donneedico.xxx_id = ids_genus_species.xxx_id;

DROP TABLE IF EXISTS ids_genus_species;