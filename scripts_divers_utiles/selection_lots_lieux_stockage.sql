SELECT lst_nom, COUNT(*) FROM t_lot_casestockage
JOIN t_lot 
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
JOIN t_lieustockage 
ON t_lieustockage.xxx_id = t_lot_casestockage.lts_lst_id
GROUP BY lst_nom
ORDER BY COUNT(*) DESC