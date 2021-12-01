DROP TABLE IF EXISTS couper_journal_annee;

SELECT xxx_id, n_ligne, doc, 
array[trim((regexp_matches(doc[1], '([a-zA-Z .]+)[0-9]{4}'))[1]), 
	trim((regexp_matches(doc[1], '[a-zA-Z .]+([0-9]{4})'))[1]),
	doc[2]] new_doc
INTO TEMPORARY TABLE couper_journal_annee
FROM all_documents
WHERE doc[1] SIMILAR TO '[a-zA-Z .]+[0-9]{4}'
AND array_length(doc, 1) = 2;

UPDATE all_documents
SET doc = new_doc
FROM couper_journal_annee
WHERE all_documents.xxx_id = couper_journal_annee.xxx_id
AND all_documents.n_ligne = couper_journal_annee.n_ligne;
