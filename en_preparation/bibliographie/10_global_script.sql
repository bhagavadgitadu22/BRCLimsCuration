DROP TABLE IF EXISTS all_documents;
DROP TABLE IF EXISTS good_documents;
DROP TABLE IF EXISTS good_documents_grouped;

CREATE TABLE all_documents (
    id serial,
	sch_identifiant varchar(32),
	doc text[],
	string_doc text,
	full_doc text
);

-- on sélectionne tous les documents référencés dans une table
-- en gardant la souche qui identifiait chaque document
-- 37727 documents
INSERT INTO all_documents(sch_identifiant, doc, string_doc, full_doc)
SELECT DISTINCT sch_identifiant,
string_to_array(trim(unnest(
	string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*', ';', 'g'), ';')
)), ',') AS doc,
trim(unnest(
	string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*', ';', 'g'), ';')
)) AS string_doc,
sch_bibliographie AS full_doc
FROM t_souche;

-- on crée aussi une table qu'on remplira au fur et à mesure avec les bons documents
CREATE TABLE good_documents (
    id serial,
	journal text,
	annee text,
	volume text,
	first_page text,
	last_page text,
	sch_identifiant varchar(32)
);

-- la même mais avec sch_identifiants regroupés
CREATE TABLE good_documents_grouped (
    id serial,
	journal text,
	annee text,
	volume text,
	first_page text,
	last_page text,
	sch_identifiants varchar[]
);
