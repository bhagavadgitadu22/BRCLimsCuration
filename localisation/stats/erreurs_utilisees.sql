SELECT don_lib, COUNT(*) 
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE don_lib NOT IN (SELECT name_en FROM world)
GROUP BY don_lib
ORDER BY COUNT(*) DESC;