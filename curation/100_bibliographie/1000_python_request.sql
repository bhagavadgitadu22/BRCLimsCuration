SELECT journal, annee, volume, first_page, sch_identifiants, n_lignes
FROM good_documents_grouped
ORDER BY random();