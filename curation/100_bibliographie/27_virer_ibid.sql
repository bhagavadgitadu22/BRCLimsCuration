DROP TABLE IF EXISTS sans_ibid;

SELECT * 
INTO TEMPORARY TABLE sans_ibid
FROM (SELECT sch_identifiant, full_doc, string_doc, doc, n_ligne, LAG(doc[1],1) OVER (
	ORDER BY sch_identifiant, n_ligne
) new_journal FROM all_documents) AS a
WHERE doc[1] LIKE '%ibid%';

UPDATE all_documents
SET doc[1] = new_journal
FROM sans_ibid
WHERE all_documents.sch_identifiant = sans_ibid.sch_identifiant
AND all_documents.n_ligne = sans_ibid.n_ligne;

UPDATE all_documents
SET doc[1] = new_journal
FROM sans_ibid
WHERE all_documents.sch_identifiant = sans_ibid.sch_identifiant
AND all_documents.n_ligne = sans_ibid.n_ligne;
