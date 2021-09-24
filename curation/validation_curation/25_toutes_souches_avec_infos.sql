SELECT * FROM t_souche
JOIN (SELECT xxx_id AS sch_col_id, col_clg_id FROM t_collection) AS tc
ON t_souche.sch_col_id = tc.sch_col_id
LEFT JOIN chemins_taxonomie
ON t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND tc.col_clg_id = chemins_taxonomie.grp_collection