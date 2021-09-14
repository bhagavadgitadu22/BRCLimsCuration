DELETE FROM t_donneedico
WHERE xxx_id NOT IN 
(SELECT DISTINCT sch_lieu FROM t_souche WHERE sch_lieu IS NOT NULL)
AND don_dic_id = 3758;
