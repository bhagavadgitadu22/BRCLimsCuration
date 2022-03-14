DROP TABLE IF EXISTS ids_taxos_a_virer;

SELECT t_donneedico.xxx_id AS taxo_id, don_lib, t_souche.xxx_id AS sch_id
INTO ids_taxos_a_virer
FROM t_donneedico
LEFT JOIN t_souche
ON t_donneedico.xxx_id = sch_taxonomie
WHERE don_dic_id = 3755
AND t_donneedico.xxx_sup_dat IS NULL
AND don_parent = 0
AND don_lib IN ('th. 0,667 et B.cereus 0,526', 'citreus', 'Vibrio piscium', 'Vibrio proteus');

UPDATE t_souche
SET sch_taxonomie = NULL
FROM ids_taxos_a_virer
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_souche.xxx_id = ids_taxos_a_virer.sch_id;

UPDATE t_donneedico 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE t_donneedico.xxx_id IN (SELECT taxo_id FROM ids_taxos_a_virer);
