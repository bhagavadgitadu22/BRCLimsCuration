/*
SELECT t_lot.xxx_id, t_souche.sch_identifiant, lot_numero, t_lot.xxx_sup_dat, t_lot.xxx_sup_usr_id
FROM t_lot 
JOIN t_donneedico 
ON lot_type = t_donneedico.xxx_id
JOIN t_souche
ON lot_sch_id = t_souche.xxx_id
WHERE don_lib = 'fiche de spécification';
*/

UPDATE t_lot
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
FROM t_donneedico 
WHERE lot_type = t_donneedico.xxx_id
AND don_lib = CONCAT('fiche de sp', CHR(233), 'cification');
