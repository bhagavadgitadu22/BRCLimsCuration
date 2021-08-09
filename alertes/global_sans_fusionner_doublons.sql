SELECT don_lib FROM t_alerte_souche 
RIGHT JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
WHERE als_alerte IS NULL
AND don_dic_id IN (2698, 2734, 2710);