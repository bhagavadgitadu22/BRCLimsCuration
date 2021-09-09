UPDATE t_lot_casestockage
SET lts_lst_id = id_balancelle,
	lts_cst_id = max+nb_row
FROM lots_et_balancelles_1
WHERE lts_lot_id = lot_id;

UPDATE t_lot_casestockage
SET lts_lst_id = id_balancelle,
	lts_cst_id = max+nb_row
FROM lots_et_balancelles_2
WHERE lts_lot_id = lot_id;
