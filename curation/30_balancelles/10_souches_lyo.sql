-- on sélectionne les lots lyophylisées de la cip
DROP TABLE IF EXISTS souches_lyophilisees;

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

SELECT t_lot.xxx_id AS lot_id, sch_identifiant, t_lieustockage.xxx_id AS stockage_id, t_lieustockage.lst_nom, array_to_string(name_path, ' > ')
INTO TABLE souches_lyophilisees
FROM t_lot

JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
JOIN t_donneedico
ON t_donneedico.xxx_id = lot_type_stockage
AND t_donneedico.xxx_sup_dat IS NULL

LEFT JOIN t_lot_casestockage
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
LEFT JOIN t_lieustockage
ON t_lieustockage.xxx_id = t_lot_casestockage.lts_lst_id
AND (t_lieustockage.xxx_id IS NULL OR t_lieustockage.xxx_sup_dat IS NULL)
LEFT JOIN rangement
ON t_lieustockage.xxx_id = rangement.xxx_id

WHERE don_lib = 'Stockage Lyophilisat'
AND (sch_identifiant SIMILAR TO 'CIP A[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{2}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{1}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP 1[0-9]{5}T?')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_lot.xxx_sup_dat IS NULL
AND sch_mot = false
AND array_to_string(name_path, ' > ') NOT SIMILAR TO '%STOCKEUR (3|4)%';
