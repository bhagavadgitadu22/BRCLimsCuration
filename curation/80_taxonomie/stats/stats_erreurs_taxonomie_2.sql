SELECT genus.don_lib AS genus, species.don_lib AS species 
FROM t_donneedico AS genus
JOIN t_donneedico AS species ON species.don_parent = genus.don_code
WHERE genus.don_dic_id = 3755 AND species.don_dic_id = 3755 AND genus.don_parent = 0
AND (LOWER(genus.don_lib), LOWER(species.don_lib)) NOT IN (SELECT LOWER(genus_name), LOWER(sp_epithet) FROM taxonomy)