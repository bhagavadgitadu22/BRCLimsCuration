UPDATE all_documents
SET string_doc = biblio_ligne
FROM dois_et_pmids
WHERE all_documents.xxx_id = dois_et_pmids.xxx_id
AND n_ligne = numero_ligne;

/*
SELECT string_doc, biblio_ligne
FROM all_documents
JOIN dois_et_pmids
ON all_documents.xxx_id = dois_et_pmids.xxx_id
WHERE n_ligne = numero_ligne
AND string_doc != biblio_ligne;
*/
