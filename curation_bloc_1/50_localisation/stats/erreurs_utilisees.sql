SELECT don_lib, don_dic_id, array_to_string(array_agg(sch_identifiant), ', '), 
array_to_string(array_agg(sch_lieu_precis), ', '), array_to_string(array_agg(sch_references_equi), ', '), 
array_to_string(array_agg(sch_bibliographie), ', '), COUNT(*) 
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE don_lib NOT IN (SELECT name_en FROM world)
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
GROUP BY don_lib, don_dic_id
ORDER BY COUNT(*) DESC;
