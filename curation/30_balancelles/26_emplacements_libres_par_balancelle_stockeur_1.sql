DROP TABLE IF EXISTS id_boite_180;
DROP TABLE IF EXISTS emplacements_libres_stockeur_1;

SELECT cst_tst_id
INTO id_boite_180
FROM t_casestockage
JOIN t_lot_casestockage
ON t_casestockage.xxx_id = lts_cst_id
JOIN ids_balancelles_1
ON ids_balancelles_1.xxx_id = lts_lst_id
WHERE t_casestockage.xxx_sup_dat IS NULL
GROUP BY cst_tst_id;

SELECT id_balancelle, lst_nom, 
id_case, cst_numero, cst_pos_x, cst_pos_y,
ROW_NUMBER() OVER (PARTITION BY id_balancelle) AS numero_case
INTO emplacements_libres_stockeur_1
FROM
(SELECT ids_balancelles_1.xxx_id AS id_balancelle, lst_nom, 
t_casestockage.xxx_id AS id_case, cst_numero, cst_pos_x, cst_pos_y
FROM ids_balancelles_1, t_casestockage
WHERE cst_tst_id IN (SELECT * FROM id_boite_180)
EXCEPT
SELECT ids_balancelles_1.xxx_id, lst_nom, 
t_casestockage.xxx_id, cst_numero, cst_pos_x, cst_pos_y
FROM t_casestockage
JOIN t_lot_casestockage
ON t_casestockage.xxx_id = lts_cst_id
JOIN ids_balancelles_1
ON ids_balancelles_1.xxx_id = lts_lst_id
WHERE t_casestockage.xxx_sup_dat IS NULL) AS a
ORDER BY lst_nom, cst_numero;

DROP TABLE IF EXISTS id_boite_180;
