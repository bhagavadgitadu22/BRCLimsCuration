SELECT COUNT(*) FROM
(SELECT don_lib
FROM t_donneedico
JOIN t_souche
ON t_souche.sch_lieu = t_donneedico.xxx_id
GROUP BY t_donneedico.xxx_id) AS a;
