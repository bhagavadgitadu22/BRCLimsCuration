WITH RECURSIVE rangement (xxx_id, level, lst_nom, name_path) AS (
    SELECT  xxx_id, 0, lst_nom, ARRAY[lst_nom::text]
    FROM    t_lieustockage
    WHERE   lst_pere_id is null

    UNION ALL

    SELECT  t1.xxx_id, t0.level + 1, t1.lst_nom, ARRAY_APPEND(t0.name_path, t1.lst_nom::text)
    FROM    t_lieustockage t1
            INNER JOIN rangement t0 ON t0.xxx_id = t1.lst_pere_id
)

SELECT rangement.xxx_id, level, lst_nom, ARRAY_TO_STRING(name_path, ' > '), COUNT(*)
FROM rangement
JOIN t_lot_casestockage
ON rangement.xxx_id = t_lot_casestockage.lts_lst_id
JOIN t_lot 
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
WHERE 'STOCKEUR 1 CIP' = ANY(name_path) OR 'STOCKEUR 2 CIP' = ANY(name_path)
GROUP BY rangement.xxx_id, level, lst_nom, name_path
ORDER BY ARRAY_TO_STRING(name_path, ' > ')