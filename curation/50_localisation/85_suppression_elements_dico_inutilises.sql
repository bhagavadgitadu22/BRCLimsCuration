UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id NOT IN 
(SELECT DISTINCT sch_lieu FROM t_souche WHERE sch_lieu IS NOT NULL)
AND don_dic_id = 3758
AND xxx_sup_dat IS NULL;
