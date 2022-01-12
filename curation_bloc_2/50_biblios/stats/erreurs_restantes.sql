SELECT * FROM all_documents 
WHERE string_doc NOT SIMILAR TO '%(doi|pmid)%';

SELECT string_doc, doc, array_agg(xxx_id), array_agg(n_ligne)
FROM all_documents 
WHERE string_doc NOT SIMILAR TO '%(doi|pmid)%'
GROUP BY string_doc, doc
ORDER BY array_length(doc, 1), length(string_doc);
