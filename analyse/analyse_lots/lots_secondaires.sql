SELECT sch_identifiant, lot_numero, lot_qte_stock, don_lib, lot_en_vente
FROM t_lot
LEFT JOIN last_version_souches_cip
ON last_version_souches_cip.xxx_id = t_lot.lot_sch_id
LEFT JOIN t_donneedico
ON t_donneedico.xxx_id = lot_type
WHERE t_lot.xxx_sup_dat IS NULL
AND don_lib = 'Lot secondaire'
ORDER BY sch_identifiant, lot_numero;


