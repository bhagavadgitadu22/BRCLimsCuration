SELECT balancelle, max, COUNT(*) FROM lots_et_balancelles_1
JOIN t_lot
ON t_lot.xxx_id = lot_id
JOIN t_donneedico
ON t_donneedico.xxx_id = lot_type_stockage
GROUP BY balancelle, max
ORDER BY COUNT(*) DESC
