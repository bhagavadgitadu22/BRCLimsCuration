SELECT * FROM t_souche
LEFT JOIN (SELECT ars_sch_id, don_lib FROM t_article_souche
LEFT JOIN t_donneedico ON ars_article = t_donneedico.xxx_id) AS tas
ON tas.ars_sch_id = t_souche.xxx_id
JOIN (SELECT xxx_id AS sch_col_id, col_clg_id FROM t_collection) AS tc
ON t_souche.sch_col_id = tc.sch_col_id
LEFT JOIN (SELECT sch_taxonomie, path, id_path FROM chemins_taxonomie) AS t_taxo
ON t_souche.sch_taxonomie = t_taxo.sch_taxonomie
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_origine
ON t_souche.sch_origine = t_origine.xxx_id
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_lieu
ON t_souche.sch_lieu = t_lieu.xxx_id
LEFT JOIN (SELECT svl_entite_id, array_agg(svl_att_id ORDER BY svl_att_id), 
		   array_agg(svl_valeur ORDER BY svl_att_id), array_agg(att_col_id ORDER BY svl_att_id) 
		   FROM t_string_val JOIN t_attribut
		   ON svl_att_id = t_attribut.xxx_id GROUP BY svl_entite_id) AS a
ON svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT cpr_sch_id, ARRAY_AGG(t_cp.cpy_numero ORDER BY cpr_cpy_id), 
		   ARRAY_AGG(cpr_resultat ORDER BY cpr_cpy_id), ARRAY_AGG(cpr_com ORDER BY cpr_cpy_id)
		   FROM t_carac_phenotypique_resultat AS t_cpr
		   JOIN t_carac_phenotypique AS t_cp
		   ON t_cp.xxx_id = t_cpr.cpr_cpy_id
		   GROUP BY cpr_sch_id) AS b
ON cpr_sch_id = t_souche.xxx_id
