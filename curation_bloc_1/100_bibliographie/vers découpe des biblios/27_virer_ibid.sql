DROP TABLE IF EXISTS sans_ibid;

SELECT * 
INTO TEMPORARY TABLE sans_ibid
FROM (SELECT xxx_id, full_doc, string_doc, doc, n_ligne, LAG(doc[1],1) OVER (
	ORDER BY xxx_id, n_ligne
) new_journal FROM all_documents) AS a
WHERE doc[1] LIKE '%ibid%';

UPDATE all_documents
SET doc[1] = new_journal
FROM sans_ibid
WHERE all_documents.xxx_id = sans_ibid.xxx_id
AND all_documents.n_ligne = sans_ibid.n_ligne;

UPDATE all_documents
SET doc[1] = new_journal
FROM sans_ibid
WHERE all_documents.xxx_id = sans_ibid.xxx_id
AND all_documents.n_ligne = sans_ibid.n_ligne;
