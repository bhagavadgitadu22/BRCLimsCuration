SELECT genus.don_lib, t_donneedico.don_lib, COUNT(*) FROM t_donneedico
JOIN t_souche ON sch_taxonomie = t_donneedico.xxx_id
JOIN t_donneedico AS genus ON t_donneedico.don_parent = genus.don_code
WHERE t_donneedico.don_dic_id = 3755 AND t_souche.xxx_id NOT IN
(SELECT t_souche.xxx_id FROM t_souche
JOIN t_donneedico AS species ON sch_taxonomie = species.xxx_id
JOIN t_donneedico AS genus ON species.don_parent = genus.don_code
WHERE species.don_dic_id = 3755 AND genus.don_dic_id = 3755
AND (genus.don_lib, species.don_lib) IN (SELECT genus_name, sp_epithet FROM taxonomy))
GROUP BY genus.don_lib, t_donneedico.don_lib
ORDER BY COUNT(*) DESC;