SELECT doc, full_doc
FROM all_documents
GROUP BY doc, full_doc
ORDER BY array_length(doc, 1);