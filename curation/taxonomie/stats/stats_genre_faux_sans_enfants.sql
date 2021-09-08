SELECT genus.don_lib
FROM t_donneedico AS genus
LEFT JOIN t_donneedico AS species
ON species.don_parent = genus.don_code
WHERE species.don_parent IS NULL
AND genus.don_dic_id = 3755
AND genus.don_parent = 0
AND genus.don_lib NOT IN (SELECT genus_name FROM taxonomy)
ORDER BY genus.don_lib