SELECT t_souche.xxx_id, sch_identifiant, sch_version, tdd_statut.don_lib, 
tdd_nature_depot.don_lib, tdd_origine.don_lib, sch_nature_prelevement, tdd_lieu.don_lib, 
tdd_depositaire.don_lib, CONCAT(tdd_redacteur.usr_prenom, ' ', tdd_redacteur.usr_nom), 
tdd_conservation.don_lib, tdd_atmosphere_incubation.don_lib, sch_temp_id,
sch_denomination, sch_synonymes, sch_references_equi, 
sch_dat_acquisition, 
sch_privee, sch_catalogue, sch_infos_catalogue, sch_mot, 
sch_mta_demandee, sch_type, sch_reference, sch_pure, sch_temps_culture, 
sch_temperature_incubation, sch_lieu_precis, sch_dat_isolement, sch_isole_par, sch_bibliographie, 
sch_qualite_numero, sch_autres_coll, tdd_classe_emballage.don_lib, sch_historique, sch_isole_a_partir_de, 
sch_ogm, sch_proprietes, tdd_type_souche.don_lib, 
pto_lib, pto_alarme, tdd_patho_plante.don_lib, tdd_patho_animal.don_lib,
t_basonyme.svl_valeur AS basonyme, t_cpc.svl_valeur AS code_produit_collection,
t_date_validation.svl_valeur AS date_de_validation, t_valeur1.svl_valeur AS valeur_1,
t_souche.xxx_cre_dat, t_souche.xxx_maj_dat, t_souche.xxx_sup_dat
FROM t_souche
LEFT JOIN t_donneedico AS tdd_nature_depot
ON tdd_nature_depot.xxx_id = sch_nature_depot
LEFT JOIN t_donneedico AS tdd_statut
ON tdd_statut.xxx_id = sch_statut
LEFT JOIN t_donneedico AS tdd_origine
ON tdd_origine.xxx_id = sch_origine
LEFT JOIN t_donneedico AS tdd_lieu
ON tdd_lieu.xxx_id = sch_lieu
LEFT JOIN t_donneedico AS tdd_depositaire
ON tdd_depositaire.xxx_id = sch_depositaire
LEFT JOIN t_utilisateur AS tdd_redacteur
ON tdd_redacteur.xxx_id = sch_redacteur
LEFT JOIN t_donneedico AS tdd_conservation
ON tdd_conservation.xxx_id = sch_conservation
LEFT JOIN t_donneedico AS tdd_atmosphere_incubation
ON tdd_atmosphere_incubation.xxx_id = sch_atmosphere_incubation
LEFT JOIN t_donneedico AS tdd_classe_emballage
ON tdd_classe_emballage.xxx_id = sch_classe_emballage
LEFT JOIN t_donneedico AS tdd_type_souche
ON tdd_type_souche.xxx_id = sch_type_souche
LEFT JOIN t_pathogenicite
ON sch_pto_id = t_pathogenicite.xxx_id
LEFT JOIN t_donneedico AS tdd_patho_plante
ON tdd_patho_plante.xxx_id = sch_patho_plante
LEFT JOIN t_donneedico AS tdd_patho_animal
ON tdd_patho_animal.xxx_id = sch_patho_animal
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Basonyme') AS t_basonyme
ON t_basonyme.att_col_id = t_souche.sch_col_id
AND t_basonyme.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Code produit collection') AS t_cpc
ON t_cpc.att_col_id = t_souche.sch_col_id
AND t_cpc.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de validation') AS t_date_validation
ON t_date_validation.att_col_id = t_souche.sch_col_id
AND t_date_validation.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Valeur 1') AS t_valeur1
ON t_valeur1.att_col_id = t_souche.sch_col_id
AND t_valeur1.svl_entite_id = t_souche.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;
