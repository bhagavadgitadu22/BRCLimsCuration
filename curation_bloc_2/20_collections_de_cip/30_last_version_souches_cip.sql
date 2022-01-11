DROP TABLE IF EXISTS last_version_souches_cip;

SELECT DISTINCT ON (sch_identifiant) 
xxx_id, sch_identifiant, sch_version, 
sch_type, sch_catalogue, 
trim(sch_denomination) AS sch_denomination,
sch_temperature_incubation, sch_temps_culture
INTO TABLE last_version_souches_cip
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND xxx_sup_dat IS NULL
ORDER BY sch_identifiant, sch_version DESC;
