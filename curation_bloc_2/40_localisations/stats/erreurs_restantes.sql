/* locs pas utilisees du tout et fausses a priori */
SELECT don_lib, don_dic_id, array_to_string(array_agg(sch_identifiant), ', '), 
array_to_string(array_agg(sch_lieu_precis), ', '), array_to_string(array_agg(sch_references_equi), ', '), 
array_to_string(array_agg(sch_bibliographie), ', '), COUNT(*) 
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IS NULL OR t_souche.xxx_sup_dat IS NOT NULL
AND don_lib NOT IN (SELECT name_en FROM world)
AND don_dic_id = 3758
GROUP BY don_lib, don_dic_id
ORDER BY COUNT(*) DESC;

/* locs utilisees et fausses a priori */
SELECT don_lib, don_dic_id, array_to_string(array_agg(sch_identifiant), ', '), 
array_to_string(array_agg(sch_lieu_precis), ', '), array_to_string(array_agg(sch_references_equi), ', '), 
array_to_string(array_agg(sch_bibliographie), ', '), COUNT(*) 
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND don_lib NOT IN (SELECT name_en FROM world)
AND don_dic_id = 3758
GROUP BY don_lib, don_dic_id
ORDER BY COUNT(*) DESC;
