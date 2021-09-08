-- on regarde le nombre d'utilisation de chaque alerte par des souches
SELECT don_lib, COUNT(*) FROM t_alerte_souche 
LEFT JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
LEFT JOIN t_souche ON als_sch_id = t_souche.xxx_id
GROUP BY don_lib
ORDER BY COUNT(*) DESC;

-- on regarde les dicos de t_donneedico où sont rangées les alertes
SELECT don_dic_id, COUNT(*) FROM t_alerte_souche 
LEFT JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
LEFT JOIN t_souche ON als_sch_id = t_souche.xxx_id
GROUP BY don_dic_id
ORDER BY COUNT(*) DESC;

-- on regarde les éléments de ces dicos qui ne sont pas utilisés dans t_alerte_souche, qui fait le lien avec t_souche
SELECT don_lib, COUNT(*) FROM t_alerte_souche 
JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
JOIN t_souche ON als_sch_id = t_souche.xxx_id
AND don_dic_id IN (2698)
AND sch_type_souche = 3752
GROUP BY t_donneedico.don_lib
ORDER BY COUNT(*) DESC;
