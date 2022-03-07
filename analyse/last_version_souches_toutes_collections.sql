DROP TABLE IF EXISTS last_version_souches;

SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_version, sch_historique, col_descr
INTO TABLE last_version_souches
FROM t_souche
LEFT JOIN t_collection
ON t_collection.xxx_id = sch_col_id
ORDER BY sch_identifiant, sch_version DESC;
