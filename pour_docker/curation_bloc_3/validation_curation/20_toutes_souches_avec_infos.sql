SELECT * FROM t_souche
JOIN (SELECT xxx_id AS sch_col_id, col_clg_id FROM t_collection) AS tc
ON t_souche.sch_col_id = tc.sch_col_id
LEFT JOIN (SELECT sch_taxonomie, path, id_path FROM chemins_taxonomie) AS t_taxo
ON t_souche.sch_taxonomie = t_taxo.sch_taxonomie
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_origine
ON t_souche.sch_origine = t_origine.xxx_id
LEFT JOIN (SELECT svl_entite_id, array_agg(svl_att_id ORDER BY svl_att_id), array_agg(svl_valeur ORDER BY svl_att_id), array_agg(att_col_id ORDER BY svl_att_id) FROM t_string_val JOIN t_attribut
ON svl_att_id = t_attribut.xxx_id GROUP BY svl_entite_id) AS a
ON svl_entite_id = t_souche.xxx_id
