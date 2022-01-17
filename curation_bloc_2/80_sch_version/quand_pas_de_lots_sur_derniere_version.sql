/*
SELECT sch_identifiant, sch_version, ARRAY_AGG(t_lot.xxx_id)
FROM t_souche
LEFT JOIN t_lot
ON t_souche.xxx_id = t_lot.lot_sch_id
WHERE (sch_identifiant = 'CIP 103286T'
OR sch_identifiant = 'CIP 104536T')
AND t_lot.xxx_sup_dat IS NULL
GROUP BY sch_identifiant, sch_version
ORDER BY sch_identifiant, sch_version;
*/

UPDATE t_lot
SET lot_sch_id = (SELECT xxx_id FROM t_souche WHERE sch_identifiant = 'CIP 103286T' AND sch_version = 5)
WHERE xxx_sup_dat IS NULL
AND lot_sch_id = (SELECT xxx_id FROM t_souche WHERE sch_identifiant = 'CIP 103286T' AND sch_version = 4);

UPDATE t_lot
SET lot_sch_id = (SELECT xxx_id FROM t_souche WHERE sch_identifiant = 'CIP 104536T' AND sch_version = 2)
WHERE xxx_sup_dat IS NULL
AND lot_sch_id = (SELECT xxx_id FROM t_souche WHERE sch_identifiant = 'CIP 104536T' AND sch_version = 1);
