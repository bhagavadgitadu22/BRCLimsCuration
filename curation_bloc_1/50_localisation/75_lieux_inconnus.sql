UPDATE t_souche
SET sch_lieu = NULL,
	sch_lieu_precis = don_lib
FROM t_donneedico
WHERE sch_lieu = t_donneedico.xxx_id
AND don_lib IN ('Shattock', 'Rivermouth', 'Bocabio', 'Carpathian mountains', 'FRG', 'Blue Lagoon lake', 'Human, blood')
AND don_dic_id IN (3758)
AND t_souche.xxx_sup_dat IS NULL
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE don_lib IN ('Shattock', 'Rivermouth', 'Bocabio', 'Carpathian mountains', 'FRG', 'Blue Lagoon lake', 'Human, blood')
AND don_dic_id = 3758
AND t_donneedico.xxx_sup_dat IS NULL;
