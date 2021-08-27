DROP TABLE IF EXISTS blabla;
DROP TABLE IF EXISTS bla;

SELECT lts_lot_id, COUNT(*)
INTO TEMPORARY TABLE blabla
FROM t_lot_casestockage
GROUP BY lts_lot_id
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;

SELECT lts_lot_id, lts_lst_id, COUNT(*)
INTO TEMPORARY TABLE bla
FROM t_lot_casestockage
GROUP BY lts_lot_id, lts_lst_id
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;

SELECT t_lot_casestockage.lts_lot_id, blabla.count, sch_identifiant, lot_numero, lst_nom
FROM t_lot_casestockage
JOIN blabla
ON t_lot_casestockage.lts_lot_id = blabla.lts_lot_id
LEFT JOIN bla
ON t_lot_casestockage.lts_lot_id = bla.lts_lot_id
JOIN t_lot 
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
JOIN t_lieustockage
ON t_lot_casestockage.lts_lst_id = t_lieustockage.xxx_id
WHERE bla.lts_lot_id IS NULL
