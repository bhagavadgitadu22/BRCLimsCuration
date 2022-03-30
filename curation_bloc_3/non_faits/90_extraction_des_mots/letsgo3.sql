SELECT t_souche.xxx_id, sch_identifiant, sch_version, t_lot.lot_numero,
--mil_numero, mil_designation_fr, mil_designation_en,
tdd_type_action.don_lib, pla_action, pla_dat_previ, pla_dat_realisation,
tdd_type_produit.don_lib, pla_remarque, pla_action_terminee, 
CONCAT(usr_prenom, ' ', usr_nom)
FROM t_souche
LEFT JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_planification
ON pla_sch_id = t_souche.xxx_id
--LEFT JOIN t_milieu
--ON pla_mil_id = t_milieu.xxx_id
--LEFT JOIN t_lotmilieu
--ON pla_lom_id = t_lotmilieu.xxx_id
LEFT JOIN t_donneedico AS tdd_type_action
ON tdd_type_action.xxx_id = pla_type_action
LEFT JOIN t_donneedico AS tdd_type_produit
ON tdd_type_produit.xxx_id = pla_type_produit
LEFT JOIN t_utilisateur
ON pla_usr_id = t_utilisateur.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;


SELECT xxx_id, sch_identifiant, sch_version, 
sch_statut, sch_nature_depot,
sch_lieu, sch_lieu_precis, 
sch_depositaire, sch_redacteur, sch_conservation, sch_atmosphere_incubation, sch_identifiant	
sch_denomination, sch_synonymes, sch_references_equi, sch_autres_coll, sch_dat_acquisition, sch_privee, sch_catalogue, sch_infos_catalogue, 
sch_mot, sch_mta_demandee, sch_type, sch_reference, sch_pure, sch_temps_culture, sch_temperature_incubation, 
sch_dat_isolement, sch_isole_par, sch_isole_a_partir_de, sch_bibliographie, sch_qualite_numero, sch_article, sch_classe_emballage, sch_historique, 
sch_ogm, sch_patho_animal, sch_proprietes, sch_type_souche, 
pto_lib, pto_alarme
basonyme, code_produit_collection, date_de_validation, valeur_1,
xxx_cre_dat, xxx_maj_dat, xxx_sup_dat
FROM t_souche
LEFT JOIN t_pathogenicite
ON sch_pto_id = t_pathogenicite.xxx_id
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
WHERE xxx_id IN (SELECT xxx_id FROM ids_mots);
