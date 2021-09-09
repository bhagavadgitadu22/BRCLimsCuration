SELECT COUNT(*) FROM
(SELECT journal, annee, volume, first_page, last_page, array_agg(sch_identifiant)
FROM good_documents
GROUP BY journal, annee, volume, first_page, last_page) AS a;