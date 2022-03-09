DROP TABLE IF EXISTS last_version_souches_lots;

SELECT t_souche.xxx_id, sch_identifiant, sch_version, lot_numero
INTO TABLE last_version_souches_lots
FROM t_souche
JOIN t_lot
ON t_souche.xxx_id = t_lot.lot_sch_id
ORDER BY xxx_id;
