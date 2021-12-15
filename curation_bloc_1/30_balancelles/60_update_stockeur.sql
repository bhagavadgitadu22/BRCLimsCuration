UPDATE t_lot_casestockage
SET lts_lst_id = lots_et_balancelles_1.id_balancelle,
	lts_cst_id = id_case
FROM lots_et_balancelles_1
JOIN emplacements_libres_stockeur_1
ON emplacements_libres_stockeur_1.id_balancelle = lots_et_balancelles_1.id_balancelle
WHERE old_id_balancelle IS NOT NULL
AND lts_lot_id = lot_id
AND numero_case = nb_row;

INSERT INTO t_lot_casestockage (xxx_vbloc, lts_lot_id, lts_cst_id, lts_lst_id)
SELECT 0, lot_id, id_case, lots_et_balancelles_1.id_balancelle 
FROM lots_et_balancelles_1
JOIN emplacements_libres_stockeur_1
ON emplacements_libres_stockeur_1.id_balancelle = lots_et_balancelles_1.id_balancelle
WHERE old_id_balancelle IS NULL
AND numero_case = nb_row;

UPDATE t_lot_casestockage
SET lts_lst_id = lots_et_balancelles_2.id_balancelle,
	lts_cst_id = id_case
FROM lots_et_balancelles_2
JOIN emplacements_libres_stockeur_2
ON emplacements_libres_stockeur_2.id_balancelle = lots_et_balancelles_2.id_balancelle
WHERE old_id_balancelle IS NOT NULL
AND lts_lot_id = lot_id
AND numero_case = nb_row;

INSERT INTO t_lot_casestockage (xxx_vbloc, lts_lot_id, lts_cst_id, lts_lst_id)
SELECT 0, lot_id, id_case, lots_et_balancelles_2.id_balancelle 
FROM lots_et_balancelles_2
JOIN emplacements_libres_stockeur_2
ON emplacements_libres_stockeur_2.id_balancelle = lots_et_balancelles_2.id_balancelle
WHERE old_id_balancelle IS NULL
AND numero_case = nb_row;
