\cd 10_collections_de_cip
\echo 10_collections_de_cip
\i 20_last_version_souches_cip.sql

\cd ../20_infos_de_dsm
\echo 20_infos_de_dsm
\i 10_create_countries.sql
\i 20_import_countries.sql
\i 30_update_countries.sql
\i 40_create_origines.sql
\i 50_import_origines.sql
\i 60_update_origines.sql

\cd ../30_genomes_p2m
\echo 30_genomes_p2m
\i 10_create_table_csv.sql
\i 20_import_infos_csv.sql
\i 30_compare_infos_p2m.sql
\i 40_souches_sans_1546.sql
\i 50_souches_avec_1546.sql
\i 60_insertions_sans_1546.sql

\cd ../40_featured_collections
\echo 40_featured_collections
\i 10_create_table_csv.sql
\i 20_import_infos_csv.sql
\i 30_infos_a_rentrer.sql

\cd ../50_articles_ogm
\echo 50_articles_ogm
\i 10_create_csv.sql
\i 20_import_csv.sql
\i 30_update_ogm_articles.sql

\cd ../60_taxos
\echo 60_taxos
\i 10_arbre_taxos.sql
\i 20_update_taxos.sql
\i 30_taxos_inutilisees.sql

\cd ../70_utilisateurs
\echo 70_utilisateurs
\i suppression_users.sql

\cd ../10_collections_de_cip
\echo 10_collections_de_cip
\i 30_suppression_tables_inutiles.sql

\cd ..
