DROP TABLE IF EXISTS all_documents;
DROP TABLE IF EXISTS good_documents;
DROP TABLE IF EXISTS good_documents_grouped;

CREATE TABLE all_documents (
    id serial,
	xxx_id integer,
	doc text[],
	string_doc text,
	full_doc text,
	n_ligne integer
);

-- on sélectionne tous les documents référencés dans une table
-- en gardant la souche qui identifiait chaque document
-- 37727 documents
INSERT INTO all_documents(xxx_id, full_doc, string_doc, doc, n_ligne)

SELECT xxx_id, full_doc, trim(arr[nr]) AS string_doc, string_to_array(trim(arr[nr]), ',') AS doc, nr AS n_ligne
FROM (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM (SELECT xxx_id, sch_bibliographie AS full_doc,
		  string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r]+', '|', 'g'), '|') AS arr 
		 FROM t_souche
		WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)) t
   ) sub
ORDER BY xxx_id, nr;

-- on crée aussi une table qu'on remplira au fur et à mesure avec les bons documents
CREATE TABLE good_documents (
    id serial,
	journal text,
	annee text,
	volume text,
	first_page text,
	last_page text,
	xxx_id integer,
	n_ligne integer
);

-- la même mais avec sch_identifiants regroupés
CREATE TABLE good_documents_grouped (
    id serial,
	journal text,
	annee text,
	volume text,
	first_page text,
	xxx_ids integer[],
	n_lignes integer[]
);