DROP TABLE IF EXISTS new_strain_designations_strings;

SELECT xxx_id, array_to_string(ARRAY_AGG(short_strain ORDER BY position), ';') AS new_string
INTO TABLE new_strain_designations_strings
FROM new_strain_designations
GROUP BY xxx_id;

/*
SELECT t_souche.xxx_maj_dat, svl_valeur, new_string, sch_historique, svl_att_id, col_nom, col_descr
FROM t_string_val
JOIN new_strain_designations_strings
ON svl_entite_id = new_strain_designations_strings.xxx_id
LEFT JOIN t_souche
ON svl_entite_id = t_souche.xxx_id
LEFT JOIN t_attribut
ON svl_att_id = t_attribut.xxx_id
LEFT JOIN t_collection
ON att_col_id = t_collection.xxx_id
WHERE svl_att_id IN (SELECT xxx_id
FROM t_attribut 
WHERE att_nom = 'Strain Designation'
AND att_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401));
*/

INSERT INTO t_string_val (svl_entite_id, svl_att_id, svl_valeur)
SELECT new_strain_designations_strings.xxx_id, 
(SELECT xxx_id FROM t_attribut WHERE att_nom = 'Strain Designation' AND att_col_id = sch_col_id), 
new_string
FROM new_strain_designations_strings
JOIN t_souche
ON t_souche.xxx_id = new_strain_designations_strings.xxx_id
LEFT JOIN t_string_val
ON svl_entite_id = new_strain_designations_strings.xxx_id
AND svl_att_id IN (SELECT xxx_id
FROM t_attribut 
WHERE att_nom = 'Strain Designation'
AND att_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401))
WHERE t_string_val.xxx_id IS NULL;

UPDATE t_string_val
SET svl_valeur = new_string
FROM new_strain_designations_strings
WHERE svl_entite_id = new_strain_designations_strings.xxx_id
AND svl_att_id IN (SELECT xxx_id
FROM t_attribut 
WHERE att_nom = 'Strain Designation'
AND att_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401));
