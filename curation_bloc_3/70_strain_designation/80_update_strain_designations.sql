DROP TABLE IF EXISTS new_strain_designations_strings;

SELECT xxx_id, array_to_string(ARRAY_AGG(short_strain ORDER BY position), ';') AS new_string
INTO TABLE new_strain_designations_strings
FROM new_strain_designations_grouped
GROUP BY xxx_id;

UPDATE t_string_val
SET svl_valeur = new_string
FROM new_strain_designations_strings
WHERE svl_entite_id = new_strain_designations_strings.xxx_id
AND svl_att_id IN (SELECT xxx_id
FROM t_attribut 
WHERE att_nom = 'Strain Designation'
AND att_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401));
