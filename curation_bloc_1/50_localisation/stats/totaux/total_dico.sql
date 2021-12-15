SELECT COUNT(*) FROM
(SELECT don_lib
FROM t_donneedico
JOIN t_souche
ON t_souche.sch_lieu = t_donneedico.xxx_id
WHERE don_dic_id IN (3758)
GROUP BY t_donneedico.xxx_id) AS a;
