SELECT t_souche.xxx_id, CASE
	WHEN sch_identifiant LIKE '%CRBIP%' THEN REPLACE(sch_identifiant, 'CRBIP', 'CRBIP ')
	ELSE sch_identifiant
END AS identifiant, sch_references_equi, '1' AS restrictions_on_use,
'1' AS nagoya,
CASE
	WHEN t_pathogenicite.pto_lib IS NOT NULL THEN t_pathogenicite.pto_lib
	ELSE '1'
END AS risk_group, 'Bacteria', 
(string_to_array(sch_denomination, ' '))[1] AS genus, CONCAT ((string_to_array(sch_denomination, ' '))[2], CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN CONCAT(' subsp. ', (string_to_array(sch_denomination, ' '))[3])
	ELSE ''
END) AS species, '',
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[A-Z]{1}[a-z]+' THEN CONCAT('var.', (string_to_array(sch_denomination, ' '))[3])
	ELSE ''
END AS infrasubspecific,
CASE
	WHEN sch_type IS True THEN 'Type'
	ELSE ''
END AS sch_type, sch_historique, 
t_deposant.don_lib, 
extract_date(t_ddr.dvl_valeur) AS date_depot, 
extract_date(sch_dat_prelevement), 
extract_date(sch_dat_isolement), 
extract_date(sch_dat_acquisition), 
sch_temperature_incubation, 
CASE 
	WHEN array_to_string(ARRAY_AGG(mil_numero), '/') != '' THEN array_to_string(ARRAY_AGG(mil_numero), '/')
	ELSE '-1'
END AS milieux,
CASE
	WHEN t_conservation.don_lib = 'Stockage Lyophilisat' THEN 'Agar'
	ELSE 'Cryo'
END AS form_of_supply, t_sd.svl_valeur AS strain_designation, 
t_lieu.don_lib, 
CASE
	WHEN sch_ogm IS False THEN 0
	ELSE 1
END AS gmo, sch_bibliographie,
CASE
	WHEN t_origine.don_lib IS NOT NULL AND sch_isole_a_partir_de != '' THEN CONCAT(t_origine.don_lib, ', ', sch_isole_a_partir_de)
	WHEN t_origine.don_lib IS NULL AND sch_isole_a_partir_de != '' THEN sch_isole_a_partir_de
	WHEN t_origine.don_lib IS NOT NULL AND sch_isole_a_partir_de = '' THEN t_origine.don_lib
	ELSE ''
END AS origine,
CONCAT('https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=', sch_identifiant) AS original_site,
sch_lieu_precis
FROM t_souche

LEFT JOIN t_pathogenicite
ON t_pathogenicite.xxx_id = sch_pto_id
LEFT JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
LEFT JOIN t_donneedico AS t_conservation
ON sch_conservation = t_conservation.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Strain Designation') AS t_sd
ON t_sd.att_col_id = t_souche.sch_col_id
AND t_sd.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, dvl_entite_id, dvl_valeur FROM t_attribut 
		   LEFT JOIN t_date_val ON t_date_val.dvl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de r??ception') AS t_ddr
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
t_sd.svl_valeur, sch_ogm, sch_bibliographie
ORDER BY t_souche.xxx_id;
