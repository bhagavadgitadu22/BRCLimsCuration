SELECT don_lib, COUNT(*) FROM t_alerte_souche 
RIGHT JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
WHERE don_dic_id IN (2698, 2734, 2710)
GROUP BY t_donneedico.xxx_id
ORDER BY COUNT(*) DESC;