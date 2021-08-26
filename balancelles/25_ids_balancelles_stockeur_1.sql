DROP TABLE IF EXISTS ids_balancelles_1;

WITH RECURSIVE rangement (xxx_id, level, lst_nom, name_path) AS (
    SELECT  xxx_id, 0, lst_nom, ARRAY[lst_nom::text]
    FROM    t_lieustockage
    WHERE   lst_pere_id is null

    UNION ALL

    SELECT  t1.xxx_id, t0.level + 1, t1.lst_nom, ARRAY_APPEND(t0.name_path, t1.lst_nom::text)
    FROM    t_lieustockage t1
            INNER JOIN rangement t0 ON t0.xxx_id = t1.lst_pere_id
)

SELECT xxx_id, lst_nom
INTO TABLE ids_balancelles_1
FROM rangement
WHERE 'STOCKEUR 1 CIP' = ANY(name_path)
AND lst_nom LIKE 'Balancelle-%'
GROUP BY xxx_id, lst_nom
ORDER BY lst_nom;
