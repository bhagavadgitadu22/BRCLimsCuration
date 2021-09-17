UPDATE t_lot_casestockage
SET lts_lst_id = lots_et_balancelles_1.id_balancelle,
	lts_cst_id = id_case
FROM lots_et_balancelles_1
JOIN emplacements_libres_stockeur_1
ON emplacements_libres_stockeur_1.id_balancelle = lots_et_balancelles_1.id_balancelle
WHERE lts_lot_id = lot_id
AND numero_case = nb_row;
--AND lts_lot_id NOT IN (659568, 4207658, 4120288, 5487786);

UPDATE t_lot_casestockage
SET lts_lst_id = lots_et_balancelles_2.id_balancelle,
	lts_cst_id = id_case
FROM lots_et_balancelles_2
JOIN emplacements_libres_stockeur_2
ON emplacements_libres_stockeur_2.id_balancelle = lots_et_balancelles_2.id_balancelle
WHERE lts_lot_id = lot_id
AND numero_case = nb_row;
--AND lts_lot_id NOT IN (659568, 4207658, 4120288, 5487786);
