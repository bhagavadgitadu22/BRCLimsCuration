SELECT don_lib, sch_lieu_precis, array_to_string(ARRAY_AGG(t_souche.xxx_id), ','), array_to_string(ARRAY_AGG(sch_identifiant), ',')
FROM t_souche
LEFT JOIN t_donneedico 
ON t_donneedico.xxx_id = sch_lieu
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY don_lib, sch_lieu_precis
ORDER BY don_lib, sch_lieu_precis;
