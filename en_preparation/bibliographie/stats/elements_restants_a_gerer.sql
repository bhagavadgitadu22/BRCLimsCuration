SELECT string_doc, full_doc
FROM all_documents
WHERE array_length(doc, 1) = 1
GROUP BY doc, string_doc, full_doc
ORDER BY char_length(string_doc);