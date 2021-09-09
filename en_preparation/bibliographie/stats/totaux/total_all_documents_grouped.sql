SELECT COUNT(*) FROM
(SELECT doc, array_agg(sch_identifiant)
FROM all_documents
GROUP BY doc
ORDER BY array_length(doc, 1)) AS a;