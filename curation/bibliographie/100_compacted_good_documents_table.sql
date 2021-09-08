INSERT INTO good_documents_grouped(journal, annee, volume, first_page, last_page, sch_identifiants)
SELECT journal, annee, volume, first_page, last_page, array_agg(sch_identifiant)
FROM good_documents
GROUP BY journal, annee, volume, first_page, last_page;