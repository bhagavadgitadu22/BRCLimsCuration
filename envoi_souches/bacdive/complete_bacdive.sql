SELECT CASE
	WHEN sch_identifiant LIKE '%CRBIP%' THEN REPLACE(sch_identifiant, 'CRBIP', 'CRBIP ')
	ELSE sch_identifiant
END AS identifier, 
sch_references_equi AS equivalent_references,
t_sd.svl_valeur AS strain_designation, 

(string_to_array(sch_denomination, ' '))[1] AS genus, 
(string_to_array(sch_denomination, ' '))[2] AS species, 
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS subspecies,
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[A-Z]{1}[a-z]+' THEN CONCAT('var. ', (string_to_array(sch_denomination, ' '))[3])
	ELSE ''
END AS infrasubspecific,
t_ba.svl_valeur AS basonym, 

CASE
	WHEN t_pathogenicite.pto_lib IS NOT NULL THEN t_pathogenicite.pto_lib
	ELSE '1'
END AS risk_group, 
sch_type AS type_strain,
CASE
	WHEN sch_ogm IS False THEN 0
	ELSE 1
END AS gmo, 

sch_historique AS history,
extract_date(sch_dat_prelevement) AS collection_date, 
extract_date(sch_dat_isolement) AS isolation_date, 
t_deposant.don_lib AS depositor,
extract_date(t_ddr.dvl_valeur) AS deposital_date, 
extract_date(sch_dat_acquisition) AS add_on_catalog_date, 

sch_temperature_incubation AS incubation_temperature, 
t_atm.don_lib AS incubation_atmosphere, 
sch_temps_culture AS time_of_culture, 
array_to_string(ARRAY_AGG(mil_designation_en), E';\n') AS growth_media,
CASE
	WHEN t_conservation.don_lib = 'Stockage Lyophilisat' THEN 'Lyo'
	ELSE 'Cryo'
END AS form_of_supply, 

t_lieu.don_lib AS country_of_origin, 
sch_lieu_precis AS specific_location_of_origin,
t_origine.don_lib AS origin_category,
sch_isole_a_partir_de AS specific_origin,

sch_bibliographie AS literature,

CONCAT('https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=', sch_identifiant) AS link_to_the_catalog

FROM t_souche
LEFT JOIN t_pathogenicite
ON t_pathogenicite.xxx_id = sch_pto_id
LEFT JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
LEFT JOIN t_donneedico AS t_atm
ON sch_atmosphere_incubation = t_atm.xxx_id
LEFT JOIN t_donneedico AS t_conservation
ON sch_conservation = t_conservation.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Strain Designation') AS t_sd
ON t_sd.att_col_id = t_souche.sch_col_id
AND t_sd.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Basonyme') AS t_ba
ON t_ba.att_col_id = t_souche.sch_col_id
AND t_ba.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, dvl_entite_id, dvl_valeur FROM t_attribut 
		   LEFT JOIN t_date_val ON t_date_val.dvl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de réception') AS t_ddr
ON t_ddr.att_col_id = t_souche.sch_col_id
AND t_ddr.dvl_entite_id = t_souche.xxx_id
LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id
LEFT JOIN t_donneedico AS t_origine
ON sch_origine = t_origine.xxx_id
LEFT JOIN (SELECT * FROM t_milieu_souche WHERE msc_standard IS True) AS tms
ON t_souche.xxx_id = msc_sch_id
LEFT JOIN t_milieu
ON msc_mil_id = t_milieu.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY t_souche.xxx_id, sch_identifiant, sch_references_equi, t_pathogenicite.pto_lib, sch_denomination, sch_type, 
sch_historique, t_deposant.don_lib, t_ddr.dvl_valeur, sch_dat_prelevement, t_origine.don_lib, sch_isole_a_partir_de, 
sch_dat_isolement, sch_dat_acquisition, sch_temperature_incubation, t_lieu.don_lib, t_conservation.don_lib, 
t_sd.svl_valeur, sch_ogm, sch_bibliographie, t_ba.svl_valeur, t_atm.don_lib
ORDER BY t_souche.xxx_id;
