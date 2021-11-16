DROP TABLE IF EXISTS differents_rangements;

WITH RECURSIVE rangement (xxx_id, level, lst_nom, name_path) AS (
    SELECT  xxx_id, 0, lst_nom, ARRAY[xxx_id]
    FROM    t_lieustockage
    WHERE   lst_pere_id is null
			AND xxx_sup_dat IS NULL

    UNION ALL

    SELECT  t1.xxx_id, t0.level + 1, t1.lst_nom, ARRAY_APPEND(t0.name_path, t1.xxx_id)
    FROM    t_lieustockage t1
    INNER JOIN rangement t0 ON t0.xxx_id = t1.lst_pere_id
	WHERE t1.xxx_sup_dat IS NULL
)

SELECT lieu, lst_nom, n_utilisations
INTO differents_rangements
FROM
(SELECT unnest(name_path) AS lieu, COUNT(*) AS n_utilisations
FROM rangement
GROUP BY lieu) AS a
JOIN t_lieustockage
ON t_lieustockage.xxx_id = lieu
WHERE t_lieustockage.xxx_sup_dat IS NULL
ORDER BY n_utilisations DESC;
