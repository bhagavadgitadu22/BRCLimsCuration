SELECT genus.don_lib AS genus, species.don_lib AS species, COUNT(*)
FROM t_donneedico AS species
JOIN t_souche
ON species.xxx_id = sch_taxonomie
LEFT JOIN t_donneedico AS genus
ON species.don_parent = genus.don_code
WHERE species.don_dic_id = 3755 AND genus.don_dic_id = 3755
AND (genus.don_lib NOT IN (SELECT genus_name FROM taxonomy WHERE genus_name IS NOT NULL)
	OR species.don_lib NOT IN (SELECT sp_epithet FROM taxonomy WHERE sp_epithet IS NOT NULL))
AND (genus.don_lib NOT IN (SELECT sp_epithet FROM taxonomy WHERE sp_epithet IS NOT NULL)
	OR species.don_lib NOT IN (SELECT subsp_epithet FROM taxonomy WHERE subsp_epithet IS NOT NULL))
GROUP BY genus.don_lib, species.don_lib
ORDER BY COUNT(*) DESC;