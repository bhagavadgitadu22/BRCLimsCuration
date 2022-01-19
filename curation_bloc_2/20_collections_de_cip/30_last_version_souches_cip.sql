DROP TABLE IF EXISTS last_version_souches_cip;

SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_version, 
sch_type, sch_catalogue, 
trim(sch_denomination) AS sch_denomination,
sch_temperature_incubation, sch_temps_culture,
svl_valeur AS basonyme, sch_synonymes,
sch_proprietes, sch_bibliographie,
t_lieu.don_lib AS lieu_origine, sch_isole_a_partir_de,
sch_dat_prelevement, sch_dat_isolement
INTO TABLE last_version_souches_cip
FROM t_souche
LEFT JOIN t_string_val
ON svl_entite_id = t_souche.xxx_id
AND svl_att_id = 2756
AND svl_valeur != ''
LEFT JOIN t_donneedico AS t_lieu
ON t_lieu.xxx_id = sch_lieu
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND t_souche.xxx_sup_dat IS NULL
ORDER BY sch_identifiant, sch_version DESC;
