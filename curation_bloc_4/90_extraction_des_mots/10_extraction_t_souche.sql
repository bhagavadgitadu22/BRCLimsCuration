SELECT e_souche.xxx_id, e_souche.xxx_cre_dat, e_souche.xxx_cre_usr, e_souche.xxx_maj_dat, e_souche.xxx_maj_usr, e_souche.xxx_sup_dat, e_souche.xxx_sup_usr, 
e_souche.sch_col_id, e_souche.sch_statut, e_souche.sch_nature_depot, e_souche.sch_taxonomie, e_souche.sch_origine, e_souche.sch_nature_prelevement, 
e_souche.sch_lieu, e_souche.sch_auteur_acquisition, e_souche.sch_depositaire, e_souche.sch_mutante, e_souche.sch_redacteur, e_souche.sch_conservation, 
e_souche.sch_atmosphere_incubation, e_souche.sch_identifiant, e_souche.sch_temp_id, e_souche.sch_cpt_id, e_souche.sch_denomination, e_souche.sch_synonymes, 
e_souche.sch_references_equi, e_souche.sch_version, e_souche.sch_remarque_version, e_souche.sch_origine_rejet, e_souche.sch_dat_acquisition, e_souche.sch_privee, 
e_souche.sch_catalogue, e_souche.sch_infos_catalogue, e_souche.sch_mot, e_souche.sch_mta_demandee, e_souche.sch_type, e_souche.sch_reference, e_souche.sch_pure, 
e_souche.sch_genotype, e_souche.sch_com_identite, e_souche.sch_prix, e_souche.sch_temps_culture, e_souche.sch_temperature_incubation, e_souche.sch_com_pheno, 
e_souche.sch_dat_pheno, e_souche.sch_lieu_precis, e_souche.sch_gps_longitude, e_souche.sch_gps_latitude, e_souche.sch_dat_prelevement, e_souche.sch_dat_isolement, 
e_souche.sch_isole_par, e_souche.sch_denomination_sujet, e_souche.sch_age_sujet, e_souche.sch_com_epidemio, e_souche.sch_com_autres, e_souche.sch_parutions_endnote, 
e_souche.sch_com_docs, e_souche.sch_bibliographie, e_souche.sch_qualite_synthese, e_souche.sch_qualite_numero, e_souche.sch_qualite_dat_approbation, 
e_souche.sch_qualite_approbateur, e_souche.sch_autres_coll, e_souche.sch_article, e_souche.sch_classe_emballage, e_souche.sch_classification, 
e_souche.sch_clinique, e_souche.sch_historique, e_souche.sch_isole_a_partir_de, e_souche.sch_ogm, e_souche.sch_patho_animal, e_souche.sch_patho_ogm, e_souche.sch_patho_plante, 
e_souche.sch_phenotype, e_souche.sch_proprietes, e_souche.sch_restriction_diffusion, e_souche.sch_references_sequence, e_souche.sch_type_souche, e_souche.sch_pto_id,

t_basonyme.svl_valeur AS basonyme, t_cpc.svl_valeur AS code_produit_collection, t_date_validation.svl_valeur AS date_de_validation, t_valeur1.svl_valeur AS valeur_1

FROM e_souche
JOIN t_souche
ON t_souche.xxx_id = e_souche.xxx_id

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

WHERE e_souche.xxx_id IN (SELECT xxx_id FROM ids_mots);
