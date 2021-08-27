SELECT don_lib, don_dic_id, array_to_string(array_agg(sch_identifiant), ', '), COUNT(*) 
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE don_lib NOT IN (SELECT name_en FROM world)
AND don_dic_id = 3758
GROUP BY don_lib, don_dic_id
ORDER BY COUNT(*) DESC;
