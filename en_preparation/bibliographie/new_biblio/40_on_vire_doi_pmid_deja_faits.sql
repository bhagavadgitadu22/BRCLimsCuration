-- on supprime les pmid et les doi de la table all_documents
DELETE FROM all_documents
WHERE LOWER(string_doc) SIMILAR TO '%(doi|pmid)%';