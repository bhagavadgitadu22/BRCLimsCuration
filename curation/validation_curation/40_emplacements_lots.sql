-- on récupère les balancelles (id et nom) du stockeur 1
DROP TABLE IF EXISTS chemins_balancelles;

WITH RECURSIVE rangement (xxx_id, level, lst_nom, name_path) AS (
    SELECT  xxx_id, 0, lst_nom, ARRAY[lst_nom::text]
    FROM    t_lieustockage
    WHERE   lst_pere_id is NULL
			AND xxx_sup_dat IS NULL

    UNION ALL

    SELECT  t1.xxx_id, t0.level + 1, t1.lst_nom, ARRAY_APPEND(t0.name_path, t1.lst_nom::text)
    FROM    t_lieustockage t1
    INNER JOIN rangement t0 ON t0.xxx_id = t1.lst_pere_id
	WHERE t1.xxx_sup_dat IS NULL
)

SELECT sch_identifiant, col_clg_id, t_lot.xxx_id, lot_numero, t_lieustockage.xxx_id, array_to_string(name_path, ' > '), array_to_string(array_agg(cst_numero ORDER BY cst_numero), ', ')
FROM t_lot
LEFT JOIN t_souche
ON lot_sch_id = t_souche.xxx_id
LEFT JOIN t_collection
ON sch_col_id = t_collection.xxx_id
LEFT JOIN t_lot_casestockage
ON lts_lot_id = t_lot.xxx_id
LEFT JOIN t_lieustockage
ON lts_lst_id = t_lieustockage.xxx_id
LEFT JOIN rangement
ON t_lieustockage.xxx_id = rangement.xxx_id
LEFT JOIN t_casestockage
ON lts_cst_id = t_casestockage.xxx_id
GROUP BY t_souche.xxx_id, t_lot.xxx_id, sch_identifiant, col_clg_id, lot_numero, t_lieustockage.xxx_id, array_to_string(name_path, ' > ');
