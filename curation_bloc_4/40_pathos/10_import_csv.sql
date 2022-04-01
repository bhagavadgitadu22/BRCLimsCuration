DROP TABLE IF EXISTS pathos_ue;

CREATE TABLE pathos_ue (
	taxo text,
	taxoshort text,
	classe text, 
	remarque text,
	souscat text
);

COPY pathos_ue (taxo, classe, remarque, souscat)
FROM 'C:/Users/Public/Documents/pathogenecite_ue_2019_utf.csv'
DELIMITER ';' CSV HEADER;

UPDATE pathos_ue
SET taxoshort = LOWER(REPLACE(REPLACE(taxo, ' subsp.', ''), ' spp.', ''))
