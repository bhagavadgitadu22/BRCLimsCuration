SELECT * FROM t_souche
JOIN (SELECT xxx_id AS sch_col_id, col_clg_id FROM t_collection) AS tc
ON t_souche.sch_col_id = tc.sch_col_id
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_lieu
ON t_souche.sch_lieu = t_lieu.xxx_id
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
LEFT JOIN (SELECT svl_entite_id, array_agg(svl_att_id ORDER BY svl_att_id), array_agg(svl_valeur ORDER BY svl_att_id) FROM t_string_val GROUP BY svl_entite_id) AS a
ON svl_entite_id = t_souche.xxx_id
