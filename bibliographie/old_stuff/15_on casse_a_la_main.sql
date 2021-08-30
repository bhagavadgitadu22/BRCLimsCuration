DROP TABLE IF EXISTS biblios_a_casser;

CREATE TABLE biblios_a_casser (
  string_doc varchar(200),
  new_string varchar(200)
);

COPY biblios_a_casser
FROM 'C:/Users/Public/Documents/separation_biblios_utf8.csv'
DELIMITER '|'
CSV;

INSERT INTO all_documents(sch_identifiant, doc, string_doc, full_doc)
SELECT sch_identifiant, string_to_array((string_to_array(new_string, ';'))[2], ','), 
(string_to_array(new_string, ';'))[2], full_doc
FROM biblios_a_casser
JOIN all_documents
ON all_documents.string_doc = biblios_a_casser.string_doc;

UPDATE all_documents
SET doc = string_to_array((string_to_array(new_string, ';'))[2], ','),
	string_doc = (string_to_array(new_string, ';'))[1]
FROM biblios_a_casser
WHERE all_documents.string_doc = biblios_a_casser.string_doc;
