DELETE FROM all_documents
WHERE LOWER(string_doc) LIKE '%submitted%'
AND array_length(doc, 1) = 1;