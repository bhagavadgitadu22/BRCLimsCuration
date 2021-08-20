SELECT journal, annee, volume, first_page, sch_identifiants
FROM good_documents_grouped
ORDER BY random()
LIMIT 300;