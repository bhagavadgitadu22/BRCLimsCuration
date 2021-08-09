SELECT don_lib, COUNT(*) 
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
GROUP BY don_lib
ORDER BY COUNT(*) DESC;