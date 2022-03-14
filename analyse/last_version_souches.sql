DROP TABLE IF EXISTS last_version_souches;

SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_version, CASE 
      WHEN sch_historique LIKE '%<-%' THEN (string_to_array(sch_historique, '<-'))[1]
      ELSE sch_historique
END AS sch_historique, sch_isole_par, don_lib AS deposant, col_descr, sch_catalogue
INTO TABLE last_version_souches
FROM t_souche
LEFT JOIN t_collection
ON t_collection.xxx_id = sch_col_id
LEFT JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
ORDER BY sch_identifiant, sch_version DESC;
