UPDATE all_documents
SET string_doc = biblio_ligne
FROM dois_et_pmids
WHERE all_documents.xxx_id = dois_et_pmids.xxx_id
AND n_ligne = numero_ligne;
