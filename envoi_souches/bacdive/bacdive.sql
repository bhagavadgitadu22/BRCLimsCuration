SELECT t_souche.xxx_id, sch_identifiant, 
sch_dat_acquisition, t_deposant.don_lib AS deposant, 
CONCAT((string_to_array(sch_denomination, ' '))[1], ' ', (string_to_array(sch_denomination, ' '))[2], ' ', CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END) AS taxon_name,
(string_to_array(sch_denomination, ' '))[1] AS genus,
(string_to_array(sch_denomination, ' '))[2] AS species,
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS subspecies,
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[A-Z]{1}[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS infrasubspecific, 
CASE
	WHEN t_pathogenicite.pto_lib IS NOT NULL THEN t_pathogenicite.pto_lib
	ELSE '1'
END AS patho_humaine, t_patho_animal.don_lib AS patho_animal, 
t_patho_plante.don_lib AS patho_plante, t_patho_ogm.don_lib AS patho_ogm, 
t_conservation.don_lib AS form_of_supply, sch_temps_culture,
sch_temperature_incubation, t_atmosphere_incubation.don_lib AS atmosphere_incubation, 
sch_type, sch_ogm,
sch_com_identite, sch_genotype, sch_autres_coll,
sch_historique, sch_proprietes,
sch_classification, sch_phenotype, 

t_ddr.svl_valeur AS date_depot, 
t_basonyme.svl_valeur AS basonyme, 
t_sd.svl_valeur AS strain_designation, 

t_lieu.don_lib AS lieu, sch_lieu_precis,
sch_dat_prelevement, sch_nature_prelevement,
sch_dat_isolement, 
t_origine.don_lib AS origine, sch_isole_a_partir_de, 

array_to_string(ARRAY_AGG(mil_designation_en), ';'),
sch_bibliographie, 
CONCAT('https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=', sch_identifiant) AS original_site
FROM t_souche

LEFT JOIN t_pathogenicite
ON t_pathogenicite.xxx_id = sch_pto_id
LEFT JOIN t_donneedico AS t_patho_animal
ON sch_patho_animal = t_patho_animal.xxx_id
LEFT JOIN t_donneedico AS t_patho_plante
ON sch_patho_plante = t_patho_plante.xxx_id
LEFT JOIN t_donneedico AS t_patho_ogm
ON sch_patho_ogm = t_patho_ogm.xxx_id
LEFT JOIN t_donneedico AS t_atmosphere_incubation
ON sch_atmosphere_incubation = t_atmosphere_incubation.xxx_id
LEFT JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
LEFT JOIN t_donneedico AS t_conservation
ON sch_conservation = t_conservation.xxx_id

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
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Basonyme') AS t_basonyme
ON t_basonyme.att_col_id = t_souche.sch_col_id
AND t_basonyme.svl_entite_id = t_souche.xxx_id

LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id
LEFT JOIN t_donneedico AS t_origine
ON sch_origine = t_origine.xxx_id
LEFT JOIN t_milieu_souche
ON t_souche.xxx_id = msc_sch_id
LEFT JOIN t_milieu
ON msc_mil_id = t_milieu.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY t_souche.xxx_id, sch_identifiant, sch_references_equi, t_pathogenicite.pto_lib, t_patho_animal.don_lib,
t_patho_plante.don_lib, t_patho_ogm.don_lib, sch_denomination, sch_type, sch_historique, t_deposant.don_lib, t_ddr.svl_valeur, 
sch_dat_prelevement, t_origine.don_lib, sch_isole_a_partir_de, sch_dat_isolement, sch_dat_acquisition, 
sch_temperature_incubation, t_atmosphere_incubation.don_lib, t_lieu.don_lib, t_conservation.don_lib, 
t_sd.svl_valeur, sch_ogm, sch_bibliographie, t_basonyme.svl_valeur
ORDER BY t_souche.xxx_id;
