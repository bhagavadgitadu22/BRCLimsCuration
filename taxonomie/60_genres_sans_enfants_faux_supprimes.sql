UPDATE t_souche
SET sch_taxonomie = NULL
WHERE t_souche.sch_taxonomie IN 
(SELECT xxx_id FROM t_donneedico
WHERE don_dic_id = 3755
AND don_parent = 0
AND don_lib IN ('102303', '109135', 'Crynéformes', 'ESSAI 100000', 'ESSAI 100001', 'Genre', 'Ommited', 'Unnamed bacterium'));

DELETE FROM t_donneedico
WHERE don_dic_id = 3755
AND don_parent = 0
AND don_lib IN ('102303', '109135', 'Crynéformes', 'ESSAI 100000', 'ESSAI 100001', 'Genre', 'Ommited', 'Unnamed bacterium');
