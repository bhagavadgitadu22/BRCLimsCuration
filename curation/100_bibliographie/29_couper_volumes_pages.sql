DROP TABLE IF EXISTS couper_volume_pages;

SELECT sch_identifiant, n_ligne, doc,
array[doc[1], doc[2],
	trim((regexp_matches(doc[3], '([0-9()]+)[: ]+e?[0-9-]+'))[1]), 
	trim((regexp_matches(doc[3], '[0-9()]+[: ]+(e?[0-9-]+)'))[1])] new_doc
INTO TEMPORARY TABLE couper_volume_pages
FROM all_documents
WHERE full_trim(doc[3]) SIMILAR TO '[0-9()]+[: ]+e?[0-9-]+'
AND array_length(doc, 1) = 3;

UPDATE all_documents
SET doc = new_doc
FROM couper_volume_pages
WHERE all_documents.sch_identifiant = couper_volume_pages.sch_identifiant
AND all_documents.n_ligne = couper_volume_pages.n_ligne;
