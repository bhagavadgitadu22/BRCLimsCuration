UPDATE t_souche
SET sch_lieu = NULL,
	sch_lieu_precis = don_lib
FROM t_donneedico
WHERE sch_lieu = t_donneedico.xxx_id
AND don_lib IN ('Shattock', 'Rivermouth', 'Bocabio', 'Carpathian mountains', 'FRG', 'Blue Lagoon lake', 'Human, blood')
AND don_dic_id IN (3758);

DELETE FROM t_donneedico
WHERE don_lib IN ('Shattock', 'Rivermouth', 'Bocabio', 'Carpathian mountains', 'FRG', 'Blue Lagoon lake', 'Human, blood')
AND don_dic_id = 3758;
