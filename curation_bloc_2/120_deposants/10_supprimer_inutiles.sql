SELECT * 
FROM t_donneedico
WHERE don_dic_id = 104
AND don_code > 2
AND xxx_id NOT IN (SELECT xxx_id FROM tous_utilises);

UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE don_dic_id = 104
AND don_code > 2
AND xxx_sup_dat IS NULL
AND xxx_id NOT IN (SELECT xxx_id FROM tous_utilises);
