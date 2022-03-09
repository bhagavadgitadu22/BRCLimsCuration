DROP TABLE IF EXISTS last_version_souches;

SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_version, lot_numero
INTO TABLE last_version_souches
FROM t_souche
LEFT JOIN t_collection
ON t_collection.xxx_id = sch_col_id
LEFT JOIN t_lot
ON t_souche.xxx_id = t_lot.lot_sch_id
ORDER BY sch_identifiant, sch_version DESC;
