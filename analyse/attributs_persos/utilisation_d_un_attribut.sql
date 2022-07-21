SELECT col_nom, t_souche.xxx_id, sch_denomination, 
sch_identifiant, tsv.svl_valeur,
sch_references_equi, tsvta.svl_valeur
FROM t_souche 
JOIN t_collection
ON sch_col_id = t_collection.xxx_id

JOIN t_string_val tsv
ON tsv.svl_entite_id = t_souche.xxx_id
JOIN t_attribut AS ta
ON tsv.svl_att_id = ta.xxx_id 
LEFT JOIN (SELECT att_nom, svl_valeur, svl_entite_id FROM t_string_val AS tsv2
JOIN t_attribut AS ta2
ON tsv2.svl_att_id = ta2.xxx_id
AND ta2.att_nom = 'Strain Designation') AS tsvta
ON t_souche.xxx_id = tsvta.svl_entite_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND ta.att_nom = 'Code produit collection'

AND tsv.svl_valeur != ''
AND sch_identifiant != tsv.svl_valeur
AND TRIM(REPLACE(sch_identifiant, 'CIP', '')) != tsv.svl_valeur
AND (REGEXP_MATCH(sch_identifiant, '[0-9]{6}') IS NULL
	 OR REGEXP_MATCH(tsv.svl_valeur, '[0-9]{6}') IS NULL
	 OR REGEXP_MATCH(sch_identifiant, '[0-9]{6}') != REGEXP_MATCH(tsv.svl_valeur, '[0-9]{6}'))
AND (REGEXP_MATCH(sch_identifiant, '[0-9]{2}.[0-9]{1,2}') IS NULL
	 OR REGEXP_MATCH(tsv.svl_valeur, '[0-9]{1,2}.[0-9]{1,2}') IS NULL
	 OR REGEXP_MATCH(sch_identifiant, '[0-9]{1,2}.[0-9]{1,2}') != REGEXP_MATCH(tsv.svl_valeur, '[0-9]{1,2}.[0-9]{1,2}'))
AND (REGEXP_MATCH(sch_identifiant, 'A[0-9]{1,3}') IS NULL
	 OR REGEXP_MATCH(tsv.svl_valeur, 'A[0-9]{1,3}') IS NULL
	 OR REGEXP_MATCH(sch_identifiant, 'A[0-9]{1,3}') != REGEXP_MATCH(tsv.svl_valeur, 'A[0-9]{1,3}'))
AND REPLACE(sch_references_equi, ' ', '') NOT LIKE CONCAT('%', REPLACE(tsv.svl_valeur, ' ', ''), '%')
AND REPLACE(tsvta.svl_valeur, ' ', '') NOT LIKE CONCAT('%', REPLACE(REPLACE(tsv.svl_valeur, ' Enterococcus', ''), ' ', ''), '%')
AND REPLACE(tsvta.svl_valeur, ' ', '') NOT LIKE CONCAT('%', REPLACE(REPLACE(REPLACE(tsv.svl_valeur, ' Enterococcus', ''), ' ', ''), '_', ''), '%')
AND col_nom = 'IEBC'

ORDER BY sch_denomination;
