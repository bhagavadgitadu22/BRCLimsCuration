SELECT t_souche.xxx_id, sch_identifiant, t_lot.xxx_id, lot_numero, lot_qte_stock, t_type_stockage.don_lib AS type_stockage

FROM t_lot
JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
LEFT JOIN t_lot_casestockage
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
LEFT JOIN t_lieustockage
ON t_lieustockage.xxx_id = t_lot_casestockage.lts_lst_id
LEFT JOIN t_donneedico AS t_type_stockage
ON t_type_stockage.xxx_id = lot_type_stockage

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM ids_mots)
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, sch_identifiant, t_lot.xxx_id, lot_numero, lot_qte_stock, mvt_code, mvt_quantite, t_stock.don_lib

FROM t_lot
JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
JOIN t_mouvementstock
ON t_lot.xxx_id = mvt_lot_id
JOIN t_donneedico AS t_stock
ON t_stock.xxx_id = lot_type_stockage

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM ids_mots)
ORDER BY t_souche.xxx_id;

