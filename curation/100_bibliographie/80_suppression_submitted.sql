DELETE FROM all_documents
WHERE LOWER(string_doc) LIKE '%submitted%'
AND array_length(doc, 1) = 1;

DELETE FROM all_documents
WHERE string_doc SIMILAR TO '(.|toto)'
AND array_length(doc, 1) = 1;

DELETE FROM all_documents
WHERE string_doc SIMILAR TO '\t'
AND array_length(doc, 1) = 1;
