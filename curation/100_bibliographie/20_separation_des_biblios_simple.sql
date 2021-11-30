DROP TABLE IF EXISTS all_documents;
DROP TABLE IF EXISTS good_documents;
DROP TABLE IF EXISTS good_documents_grouped;

CREATE TABLE all_documents (
    id serial,
	sch_identifiant varchar(32),
	doc text[],
	string_doc text,
	full_doc text,
	n_ligne integer
);

-- on sélectionne tous les documents référencés dans une table
-- en gardant la souche qui identifiait chaque document
-- 37727 documents
INSERT INTO all_documents(sch_identifiant, full_doc, string_doc, doc, n_ligne)

SELECT DISTINCT sch_identifiant, full_doc, trim(arr[nr]) AS string_doc, string_to_array(trim(arr[nr]), ',') AS doc, nr AS n_ligne
FROM (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM (SELECT sch_identifiant, sch_bibliographie AS full_doc,
		  string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r]+', '|', 'g'), '|') AS arr 
		 FROM t_souche
		WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)) t
   ) sub
ORDER BY sch_identifiant, nr;
