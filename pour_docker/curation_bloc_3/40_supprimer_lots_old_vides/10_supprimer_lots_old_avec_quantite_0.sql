/*
SELECT * 
FROM t_lot
WHERE lot_numero LIKE '%old%'
AND lot_qte_stock = 0
AND xxx_sup_dat IS NULL;
*/

UPDATE t_lot
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE lot_numero LIKE '%old%'
AND lot_qte_stock = 0
AND xxx_sup_dat IS NULL;
