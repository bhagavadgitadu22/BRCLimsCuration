SELECT xxx_id, sch_denomination, sch_identifiant, sch_version, 
CASE 
	WHEN sch_references_equi != '' AND svl_valeur != '' THEN CONCAT(sch_references_equi, ';', svl_valeur)
	WHEN sch_references_equi = '' AND svl_valeur != '' THEN svl_valeur
	WHEN sch_references_equi != '' AND svl_valeur = '' THEN sch_references_equi
	ELSE ''
END, sch_references_equi, svl_valeur
FROM t_souche 
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Strain Designation') AS t_basonyme
ON t_basonyme.att_col_id = t_souche.sch_col_id
AND t_basonyme.svl_entite_id = t_souche.xxx_id
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND (sch_denomination SIMILAR TO '% (sp.|species|like|spp.|sp )%' OR sch_denomination LIKE '% sp');
