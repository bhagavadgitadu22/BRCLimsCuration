\cd 10_fonctions
\echo 10_fonctions
\i 0_full_trim.sql
\i 10_custom_order.sql

\cd ../20_collections_de_cip
\echo 20_collections_de_cip
\i liste_souches_bon_brclims.sql

\cd ../30_balancelles
\echo 30_balancelles
\i 10_souches_lyo.sql
\i 20_excel_stockeur_1.sql
\i 25_ids_balancelles_stockeur_1.sql
\i 26_emplacements_libres_par_balancelle_stockeur_1.sql
\i 30_excel_stockeur_2.sql
\i 35_ids_balancelles_stockeur_2.sql
\i 36_emplacements_libres_par_balancelle_stockeur_2.sql
\i 40_correspondance_lots_balancelles_stockeur_1.sql
\i 50_correspondance_lots_balancelles_stockeur_2.sql
\i 60_update_stockeur.sql
\i 70_differents_rangements.sql
\i 80_supprimer_lieux_stockage_vides.sql
\i 90_supprimer_tables_inutiles.sql

\cd ../40_historique_bacillus
\echo 40_historique_bacillus
\i 0_souches_a_modifier.sql
\i 5_virer_strains_ok.sql
\i 0_souches_a_modifier.sql
\i 10_numero_de_strain.sql
\i 15_lines_historique.sql
\i 20_on_vire_partie_cip.sql
\i 30_correct_lines.sql
\i 40_new_historiques.sql
\i 50_suppression_tables.sql

\cd ../50_localisation
\echo 50_localisation
\i 10_english_world.sql
\i 11_french_world.sql
\i 12_mixed_world.sql
\i 15_cities.sql
\i 20_trim_elements_localisation.sql
\i 25_de_francais_a_anglais.sql
\i 26_ajout_majuscules_et_virer_accents.sql
\i 30_virer_uk_et_usa.sql
\i 35_virer_erreurs_orthographe_pays.sql
\i 36_autres_erreurs_orthographe.sql
\i 37_erreurs_orthographe_villes.sql
\i 38_erreurs_a_souches_multiples.sql
\i 39_peaufinage_par_souches.sql
\i 60_separation_ville_de_pays_pour_format_virgule.sql
\i 61_separation_ville_de_pays_pour_format_virgule_inverse.sql
\i 62_extraction_de_parentheses.sql
\i 65_de_ville_a_pays.sql
\i 30_virer_uk_et_usa.sql
\i 35_virer_erreurs_orthographe_pays.sql
\i 70_pays_restants_dans_lieux.sql
\i 75_lieux_inconnus.sql
\i 80_suppression_doublons_de_lieux.sql
\i 85_suppression_elements_dico_inutilises.sql
\i 90_correction_lieux_precis.sql
\i 100_suppression_tables_inutiles.sql

\cd ../60_pathogenicite
\echo 60_pathogenicite
\i update_champs_patho_animal.sql

\cd ../70_souches_2xxxxx
\echo 70_souches_2xxxxx
\i liste_des_200000_supprimables.sql

\cd ../80_taxonomie
\echo 80_taxonomie
\i 10_table_taxonomie_lpsn.sql
\i 14_pas_de_souche_degage.sql
\i 15_trim_elements_taxo.sql
\i 16_accents_vires.sql
\i 20_update_champs_divers.sql
\i 30_enteroccus.sql
\i 40_erreurs_orthographe_genus_ou_species.sql
\i 41_genus_en_majuscules.sql
\i 50_inserer_taxos_manquantes.sql
\i 60_casser_en_2_genus_species.sql
\i 70_erreurs_genus_deduites_de_lehvenshtein.sql
\i 71_erreurs_genus_deduites_de_trigrammes.sql
\i 80_supprimer_erreurs_pas_dans_souches.sql
\i 81_virer_serovar.sql
\i 90_suppression_doublons_taxo.sql
\i 100_suppression_table_taxonomy.sql

\cd ../90_temperature
\echo 90_temperature
\i vers_de_vrais_nombres.sql

\cd ../100_bibliographie
\echo 100_bibliographie
\i 5_points_virgules_en_trop.sql
\i 10_biblios_plus_propres.sql
\i 20_quelques_corrections_manuelles.sql

\cd ../100_bibliographie
\echo 100_bibliographie
\i 0_array_unique_stable.sql
\i 5_points_virgules_en_trop.sql
\i 10_biblios_plus_propres.sql
\i 15_quelques_corrections_manuelles.sql
\i 20_separation_des_biblios_simple.sql
\i 25_trim_lignes.sql
\i 30_import_infos_csv.sql
\i 40_update_biblios.sql
\i 50_update_sch_biblios.sql

\cd ../20_collections_de_cip
\echo 20_collections_de_cip
\i suppression_table_inutile.sql
