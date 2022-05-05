SELECT * FROM t_souche
JOIN (SELECT xxx_id AS sch_col_id, col_clg_id FROM t_collection) AS tc
ON t_souche.sch_col_id = tc.sch_col_id
LEFT JOIN (SELECT xxx_id, pto_lib FROM t_pathogenicite) AS t_patho
ON t_patho.xxx_id = sch_pto_id
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_lieu
ON t_lieu.xxx_id = sch_lieu
LEFT JOIN (SELECT sch_taxonomie, path, id_path FROM chemins_taxonomie) AS t_taxo
ON t_souche.sch_taxonomie = t_taxo.sch_taxonomie
LEFT JOIN (SELECT xxx_id, don_lib, don_dic_id FROM t_donneedico) AS t_origine
ON t_souche.sch_origine = t_origine.xxx_id
