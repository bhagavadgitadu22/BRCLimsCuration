SELECT don_lib, COUNT(*)
FROM t_donneedico 
JOIN t_souche
ON t_donneedico.xxx_id = sch_taxonomie
WHERE don_dic_id = 3755 
AND don_lib NOT IN (SELECT genus_name FROM taxonomy WHERE genus_name IS NOT NULL)
AND don_lib NOT IN (SELECT sp_epithet FROM taxonomy WHERE sp_epithet IS NOT NULL)
AND don_lib NOT IN (SELECT subsp_epithet FROM taxonomy WHERE subsp_epithet IS NOT NULL)
GROUP BY don_lib
ORDER BY COUNT(*) DESC;