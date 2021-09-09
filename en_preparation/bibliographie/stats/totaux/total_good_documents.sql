SELECT COUNT(*) FROM
(SELECT journal, annee, volume, first_page, last_page, sch_identifiant
FROM good_documents) AS a;