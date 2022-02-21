\cd 10_collections_de_cip
\echo 10_collections_de_cip
\i 10_liste_souches_bon_brclims.sql
\i 20_last_version_souches_cip.sql

\cd ../20_supprimer_lots_old_vides
\echo 20_supprimer_lots_old_vides
\i 10_supprimer_lots_old_avec_quantite_0.sql

\cd ../30_mettre_infos_care
\echo 30_mettre_infos_care
\i 10_create_table_csv.sql
\i 20_import_csv_care.sql
\i 30_mettre_infos_dans_tables.sql

\cd ../40_taxonomie
\echo 40_taxonomie
\i 10_quelques_taxonomies_a_virer.sql
\i 20_cas_des_photorhabdus.sql

\cd ../50_isolats
\echo 50_isolats
\i 10_reformattage_isole_a_partir_de.sql
\i 20_create_table_csv.sql
\i 30_import_csv_traductions.sql
\i 40_update_avec_traductions.sql
\i 50_trim_correctement_isolats.sql

\cd ../60_origine
\echo 60_origine
\i 10_origine_animal.sql
\i 11_origine_environnement.sql
\i 12_origine_food.sql
\i 13_origine_humaine.sql
\i 14_origine_plante.sql
\i 20_termes_generiques_restants.sql
\i 30_soil.sql
\i 31_water.sql
\i 32_divers_environment.sql
\i 40_derives_d_humains.sql
\i 50_animaux.sql
\i 51_insectes_chelous.sql
\i 52_larves.sql
\i 53_moutons.sql
\i 60_divers_nourritures.sql

\cd ../70_strain_designation
\echo 70_strain_designation
\i 0_table_taxonomie_lpsn.sql
\i 10_extraction_strains.sql
\i 20_virer_strains_especes.sql
\i 25_vers_bad_strains.sql
\i 30_casser_les_egaux.sql
\i 31_casser_les_strains.sql
\i 35_bad_spelling_cip.sql
\i 40_bilan_des_collections.sql
\i 45_separation_en_refs_equis_ou_strain_designations.sql
\i 50_refs_equis_dans_new_refs_equis.sql
\i 55_prepare_new_refs_equis_grouped.sql
\i 60_update_refs_equis.sql
\i 70_prepare_new_strain_designations_grouped.sql
\i 80_update_strain_designations.sql

\cd ../10_collections_de_cip
\echo 10_collections_de_cip
\i 30_suppression_tables_inutiles.sql
