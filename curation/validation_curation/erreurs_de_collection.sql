SELECT * 
FROM t_souche
JOIN t_collection
ON sch_col_id = t_collection.xxx_id
JOIN t_donneedico
ON sch_lieu = t_donneedico.xxx_id
LEFT JOIN t_dico
ON don_dic_id = t_dico.xxx_id
WHERE CONCAT('[', col_clg_id, ']') != dic_grp_collection
ORDER BY t_souche.xxx_id;