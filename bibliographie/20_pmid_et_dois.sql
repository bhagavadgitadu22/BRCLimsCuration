-- on supprime les pmid et les doi de la table all_documents
DELETE FROM all_documents
WHERE LOWER(string_doc) SIMILAR TO '%(doi|pmid)%';

-- on supprime aussi les éléments null de all_documents
DELETE FROM all_documents 
WHERE array_length(doc, 1) IS NULL;