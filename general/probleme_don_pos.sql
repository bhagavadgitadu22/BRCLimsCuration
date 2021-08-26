SELECT don_pos, don_lib, don_dic_id
FROM t_souche 
LEFT JOIN t_donneedico
ON t_donneedico.xxx_id = sch_lieu
WHERE don_dic_id = 3758
GROUP BY don_pos, don_lib, don_dic_id
ORDER BY don_pos;
