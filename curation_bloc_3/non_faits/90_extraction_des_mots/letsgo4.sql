SELECT xxx_id, xxx_cre_dat, xxx_maj_dat, xxx_sup_dat, sch_statut, 
sch_nature_depot, sch_taxonomie, sch_origine, sch_nature_prelevement, sch_lieu, sch_depositaire, 
sch_redacteur, sch_conservation, sch_atmosphere_incubation, sch_identifiant, sch_temp_id,
sch_cpt_id, sch_denomination, sch_synonymes, sch_references_equi, sch_version, 
sch_dat_acquisition, sch_privee, sch_catalogue, sch_infos_catalogue, sch_mot, 
sch_mta_demandee, sch_type, sch_reference, sch_pure, sch_temps_culture, 
sch_temperature_incubation, sch_lieu_precis, sch_dat_isolement, sch_isole_par, sch_bibliographie, 
sch_qualite_numero, sch_autres_coll, sch_classe_emballage, sch_historique, sch_isole_a_partir_de, 
sch_ogm, sch_proprietes, sch_type_souche, sch_pto_id, sch_patho_plante, 
sch_patho_animal
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'public'
AND table_name = 't_souche'
