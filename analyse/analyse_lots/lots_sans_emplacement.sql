DROP TABLE IF EXISTS lots_sans_emplacement;

SELECT sch_identifiant, t_lot.xxx_id, lot_numero, lot_qte_stock, don_lib
FROM t_lot
LEFT JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
LEFT JOIN t_lot_casestockage
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
LEFT JOIN t_lieustockage
ON t_lieustockage.xxx_id = t_lot_casestockage.lts_lst_id
LEFT JOIN t_donneedico
ON t_donneedico.xxx_id = lot_type_stockage
WHERE (t_lot_casestockage.xxx_id IS NULL
OR t_lieustockage.xxx_id IS NULL)
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_lot.xxx_sup_dat IS NULL
ORDER BY sch_identifiant, lot_numero;


