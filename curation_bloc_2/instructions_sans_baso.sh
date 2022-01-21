\cd 20_collections_de_cip
\echo 20_collections_de_cip
\i 10_liste_souches_bon_brclims.sql

\cd ../30_historiques
\echo 30_historiques
\i 0_table_taxonomie_lpsn.sql
\i 10_correct_guillemets_strains.sql
\i 15_erreurs_des_3_points_virgules.sql
\i 16_corriger_fleches_entre_proprios.sql
\i 17_date_arrivee_souches_jfcharles.sql
\i 18_autres_corrections.sql
\i 20_extraction_strains.sql
\i 25_virer_strains_especes.sql
\i 26_vers_bad_strains.sql
\i 27_update_all_strains.sql
\i 28_bad_spelling_cip.sql
\i 30_sanitiser_refs_equis.sql
\i 40_update_refs_equis.sql
\i 49_preparation_virage_doublons.sql
\i 50_virer_doublons_refs_equis.sql
\i 60_virer_tables_temporaires.sql
\i 40_virer_tables_temporaires.sql

\cd ../40_localisations
\echo 40_localisations
\i 10_vers_south_korea_for_cities.sql
\i 20_separation_ville_pays.sql
\i 30_supprimer_doublons_dico.sql

\cd ../50_biblios
\echo 50_biblios
\i 10_update_DOI.sql
\i 20_pas_de_double_virgule.sql

\cd ../20_collections_de_cip
\echo 20_collections_de_cip
\i 30_last_version_souches_cip.sql

\cd ../60_temp_et_baso
\echo 60_temp_et_baso
\i 0_denominations_mal_formattees.sql
\i 10_souches_types_de_souches.sql
\i 20_nettoyer_temps_culture.sql
\i 30_nettoyer_basonymes.sql
\i 50_update_temperatures.sql
\i 60_update_temps_culture.sql
