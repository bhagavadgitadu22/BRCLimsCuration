\cd 20_collections_de_cip
\echo 20_collections_de_cip
\i 10_liste_souches_bon_brclims.sql

\cd ../30_historiques
\echo 30_historiques
\i 10_correct_guillemets_strains.sql
\i 15_erreurs_des_3_points_virgules.sql
\i 16_corriger_fleches_entre_proprios.sql
\i 17_date_arrivee_souches_jfcharles.sql
\i 18_autres_corrections.sql
\i 19_dates_dans_lignes_historiques.sql
\i 20_extraction_strains.sql
\i 25_suppressions_souches_de_strains_r.sql
\i 30_sanitiser_refs_equis.sql
\i 40_virer_tables_temporaires.sql

\cd ../40_localisations
\echo 40_localisations
\i 10_vers_south_korea_for_cities.sql
\i 20_separation_ville_pays.sql
\i 30_supprimer_doublons_dico.sql
\i 40_suppression_des_dates.sql
\i 50_virer_tables_temporaires.sql

\cd ../50_biblios
\echo 50_biblios
\i 1_pas_de_double_virgule.sql
\i 2_pas_de_virgule_dans_titre_journal.sql
\i 10_create_table_csv.sql
\i 15_import_infos_csv.sql
\i 20_separation_des_biblios_simples.sql
\i 30_update_biblios.sql
\i 40_update_sch_biblios.sql
\i 50_isjem.sql
\i 60_drop_tables_temporaires.sql

\cd ../20_collections_de_cip
\echo 20_collections_de_cip
\i 20_last_version_souches_cip.sql

\cd ../60_temp_et_baso
\echo 60_temp_et_baso
\i 0_denominations_mal_formattees.sql
\i 10_souches_types_de_souches.sql
\i 20_nettoyer_temps_culture.sql
\i 30_nettoyer_basonymes.sql

\cd ../20_collections_de_cip
\echo 20_collections_de_cip
\i 20_last_version_souches_cip.sql

\cd ../60_temp_et_baso
\echo 60_temp_et_baso
\i 50_update_temperatures.sql
\i 60_update_temps_culture.sql
\i 70_update_basonymes.sql
\i 80_virer_tables_temporaires.sql

\cd ../70_supprimer_cip_e
\echo 70_supprimer_cip_e
\i 10_supprimer_souches_cip_e.sql
\i 20_changer_denomination_lorsque_absente.sql

\cd ../80_sch_version
\echo 80_sch_version
\i quand_pas_de_lots_sur_derniere_version.sql

\cd ../90_deposants
\echo 90_deposants
\i 0_une_seule_virgule.sql
\i 5_deposants_utilises.sql
\i 10_supprimer_inutiles.sql
\i 12_gestion_des_solistes.sql
\i 15_mettre_a_jour_instituts.sql
\i 18_mettre_a_jour_souches.sql
\i 20_supprimer_doublons.sql
\i 30_virer_tables_temporaires.sql

\cd ../100_fiches_de_specification
\echo 100_fiches_de_specification
\i 10_suppression_lots_qui_sont_fiches.sql

\cd ../20_collections_de_cip
\echo 20_collections_de_cip
\i 30_suppression_tables_inutiles.sql
