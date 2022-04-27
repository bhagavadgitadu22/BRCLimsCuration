SELECT att_entite_ref, att_nom, att_typ, ARRAY_AGG(att_col_id) FROM t_attribut GROUP BY att_entite_ref, att_nom, att_typ;

SELECT *
FROM t_attribut 
LEFT JOIN t_string_val 
ON t_string_val.svl_att_id = t_attribut.xxx_id
WHERE att_nom = 'Basonyme'
