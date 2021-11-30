UPDATE all_documents
SET string_doc = biblio_ligne
FROM dois_et_pmids
WHERE sch_identifiant = identifiant 
AND n_ligne = numero_ligne;
