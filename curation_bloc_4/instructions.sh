\cd 10_collections_de_cip
\echo 10_collections_de_cip
\i 10_last_version_souches_cip.sql
\i 20_table_taxonomie_lpsn.sql

\cd ../20_origine
\echo 20_origine
\i 10_virer_environment_de_isole_a_partir_de.sql
\i 20_virer_human_de_isole_a_partir_de.sql
\i 25_virer_only_human_aussi.sql
\i 30_virer_animal_de_isole_a_partir_de.sql

\cd ../30_pathos
\echo 30_pathos
\i 10_import_csv.sql
\i 20_compa.sql

\cd ../40_milieux
\echo 40_milieux
\i suppression_661_et_718.sql

\cd ../50_refs_equis
\echo 50_refs_equis
\i doublons_et_cpc.sql

\cd ../60_extraction_des_mots
\echo 60_extraction_des_mots
\i tentative_de_suppression_mots.sql

\cd ../70_country_of_origin_unknown
\echo 70_country_of_origin_unknown
\i vers_unknown_dans_lieu.sql

\cd ../80_decaler_info_de_collection
\echo 80_decaler_info_de_collection
\i move.sql

\cd ../90_de_denoms_a_taxos
\echo 90_de_denoms_a_taxos
\i 10_denoms_sans_taxos.sql
\i 30_parenteles_taxonomie.sql
\i 40_taxos_a_ajouter_dans_dico.sql
\i 50_ajout_genus.sql
\i 51_ajout_species.sql
\i 52_ajout_subspecies.sql
\i 60_parenteles_taxonomie.sql
\i 70_mise_a_jour_taxos.sql

\cd ../10_collections_de_cip
\echo 10_collections_de_cip
\i 30_suppression_tables_inutiles.sql

\cd ..
