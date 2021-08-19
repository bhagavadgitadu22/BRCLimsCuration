SELECT COUNT(*), journal, annee, volume, first_page, last_page, sch_identifiant
FROM good_documents
GROUP BY journal, annee, volume, first_page, last_page, sch_identifiant
HAVING COUNT(*)>1
ORDER BY COUNT(*) DESC;