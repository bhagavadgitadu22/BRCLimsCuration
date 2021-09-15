UPDATE t_lot_casestockage
SET lts_lst_id = id_balancelle,
	lts_cst_id = (SELECT xxx_id FROM t_casestockage WHERE cst_numero = 110+nb_row AND cst_tst_id = 4647877)
FROM lots_et_balancelles_1
WHERE lts_lot_id = lot_id;

UPDATE t_lot_casestockage
SET lts_lst_id = id_balancelle,
	lts_cst_id = (SELECT xxx_id FROM t_casestockage WHERE cst_numero = 110+nb_row AND cst_tst_id = 4647877)
FROM lots_et_balancelles_2
WHERE lts_lot_id = lot_id;
