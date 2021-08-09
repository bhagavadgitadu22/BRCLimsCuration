SELECT don_lib, COUNT(*) FROM t_alerte_souche 
LEFT JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
LEFT JOIN t_souche ON als_sch_id = t_souche.xxx_id
GROUP BY don_lib
ORDER BY COUNT(*) DESC;