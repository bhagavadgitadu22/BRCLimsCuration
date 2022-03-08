DROP TABLE IF EXISTS last_version_souches;

SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_version, sch_historique, 
col_descr, sch_isole_par, t_deposant.don_lib AS deposant
INTO TABLE last_version_souches
FROM t_souche
LEFT JOIN t_collection
ON t_collection.xxx_id = sch_col_id
LEFT JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
ORDER BY sch_identifiant, sch_version DESC;
