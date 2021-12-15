SELECT ARRAY_AGG(sch_identifiant), ARRAY_AGG(don_lib), sch_lieu_precis 
FROM t_souche 
JOIN t_donneedico
ON t_donneedico.xxx_id = sch_lieu
WHERE don_dic_id = 3758
AND sch_lieu_precis SIMILAR TO '%;%' GROUP BY sch_lieu_precis;
