SELECT t_souche.xxx_id, sch_identifiant, sch_references_equi, '1' AS restrictions_on_use,
'1' AS nagoya, '', '', '', t_pathogenicite.pto_lib, '', '', 'Bacteria', 
CONCAT((string_to_array(sch_denomination, ' '))[1], ' ', (string_to_array(sch_denomination, ' '))[2], ' subsp. ', CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END) AS taxon_name,
CONCAT('var.', CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[A-Z]{1}[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END) AS infrasubspecific, '', 
CASE
	WHEN sch_type IS True THEN 'Type'
	ELSE ''
END AS statut, sch_historique, 
t_deposant.don_lib, t_ddr.svl_valeur AS date_depot, 
'', sch_dat_prelevement, 
'', sch_dat_isolement, 
sch_dat_acquisition, '', 
sch_temperature_incubation, 
array_to_string(ARRAY_AGG(mil_numero), ';'),
t_conservation.don_lib AS form_of_supply, t_sd.svl_valeur AS strain_designation, 
'', '', t_lieu.don_lib, sch_ogm, '', '', '', sch_bibliographie, 
'', '', '', '', '', '', '', '', '', '', sch_isole_a_partir_de, '',  '',  '',  '', 
CONCAT('https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=', sch_identifiant) AS original_site
FROM t_souche

LEFT JOIN t_pathogenicite
ON t_pathogenicite.xxx_id = sch_pto_id
LEFT JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
LEFT JOIN t_donneedico AS t_conservation
ON sch_depositaire = t_conservation.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Strain Designation') AS t_sd
ON t_sd.att_col_id = t_souche.sch_col_id
AND t_sd.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de réception') AS t_ddr
ON t_ddr.att_col_id = t_souche.sch_col_id
AND t_ddr.svl_entite_id = t_souche.xxx_id
LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id
LEFT JOIN t_milieu_souche
ON t_souche.xxx_id = msc_sch_id
LEFT JOIN t_milieu
ON msc_mil_id = t_milieu.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY t_souche.xxx_id, sch_identifiant, sch_references_equi, t_pathogenicite.pto_lib, sch_denomination, sch_type, 
sch_historique, t_deposant.don_lib, t_ddr.svl_valeur, sch_dat_prelevement, sch_isole_a_partir_de, 
sch_dat_isolement, sch_dat_acquisition, sch_temperature_incubation, t_lieu.don_lib, t_conservation.don_lib, 
t_sd.svl_valeur, sch_ogm, sch_bibliographie
ORDER BY t_souche.xxx_id;
