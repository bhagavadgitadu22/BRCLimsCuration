SELECT * FROM all_documents 
WHERE array_length(doc, 1) = 5
AND doc[1] SIMILAR TO '%[a-zA-Z]+%'
AND doc[2] SIMILAR TO '[0-9]{4}'
AND doc[4] SIMILAR TO '[0-9]+'
AND doc[5] SIMILAR TO '%(doi|pmid)%';

SELECT *
FROM all_documents 
WHERE string_doc SIMILAR TO '%(doi|pmid)%'
AND NOT(array_length(doc, 1) = 5
AND doc[1] SIMILAR TO '%[a-zA-Z]+%'
AND doc[2] SIMILAR TO '[0-9]{4}'
AND doc[4] SIMILAR TO '[0-9]+'
AND doc[5] SIMILAR TO '%(doi|pmid)%');
