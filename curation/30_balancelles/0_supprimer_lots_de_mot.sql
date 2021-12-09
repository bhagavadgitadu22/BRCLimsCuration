/*
SELECT sch_identifiant, lot_numero, sch_mot, lot_qte_stock
FROM t_lot
JOIN t_souche
ON lot_sch_id = t_souche.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_lot.xxx_sup_dat IS NULL
AND sch_mot = true;
*/

UPDATE t_lot
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
FROM t_souche
WHERE lot_sch_id = t_souche.xxx_id
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_lot.xxx_sup_dat IS NULL
AND sch_mot = true
AND lot_qte_stock = 0;
