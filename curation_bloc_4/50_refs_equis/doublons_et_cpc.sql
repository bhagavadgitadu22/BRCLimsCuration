DROP TABLE IF EXISTS strains_classees;
DROP TABLE IF EXISTS refs_equis_a_garder;
DROP TABLE IF EXISTS new_refs_equis;
DROP TABLE IF EXISTS refs_equis_a_supprimer;

SELECT xxx_id, sch_references_equi, arr[nr] AS ref_equi, nr AS number_row, svl_valeur AS strain_designation
INTO strains_classees
FROM  (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM  (SELECT t_souche.xxx_id, sch_references_equi, string_to_array(sch_references_equi, ';') AS arr, svl_valeur 
		  FROM t_souche 
		  JOIN t_attribut
		  ON att_col_id = sch_col_id
		  AND att_nom = 'Strain Designation'
		  LEFT JOIN t_string_val
		  ON svl_entite_id = t_souche.xxx_id
		  AND svl_att_id = t_attribut.xxx_id
		  WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)) t
   ) sub;

SELECT xxx_id, sch_references_equi, array_to_string(ARRAY_AGG(ref_equi ORDER BY number_row), ';') AS new_string
INTO refs_equis_a_garder
FROM strains_classees
WHERE (strain_designation IS NULL OR strain_designation NOT LIKE CONCAT('%', ref_equi, '%'))
AND ref_equi NOT LIKE CONCAT('%CPC%')
GROUP BY xxx_id, sch_references_equi;

SELECT xxx_id, sch_references_equi, strain_designation
INTO refs_equis_a_supprimer
FROM strains_classees
WHERE xxx_id NOT IN (SELECT xxx_id FROM refs_equis_a_garder)
GROUP BY xxx_id, sch_references_equi, strain_designation;

UPDATE t_souche
SET sch_references_equi = ''
FROM refs_equis_a_supprimer
WHERE t_souche.xxx_id = refs_equis_a_supprimer.xxx_id;
