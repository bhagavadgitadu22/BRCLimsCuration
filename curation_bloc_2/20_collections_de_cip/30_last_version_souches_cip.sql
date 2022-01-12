DROP TABLE IF EXISTS last_version_souches_cip;

SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_version, 
sch_type, sch_catalogue, 
trim(sch_denomination) AS sch_denomination,
sch_temperature_incubation, sch_temps_culture,
svl_valeur AS basonyme, sch_synonymes
INTO TABLE last_version_souches_cip
FROM t_souche
LEFT JOIN t_string_val
ON svl_entite_id = t_souche.xxx_id
AND svl_att_id = 2756
AND svl_valeur != ''
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND xxx_sup_dat IS NULL
ORDER BY sch_identifiant, sch_version DESC;
