DROP TABLE IF EXISTS dois_et_pmids;

CREATE TABLE dois_et_pmids (
  xxx_id integer,
  numero_ligne integer,
  biblio_ligne text
);

COPY dois_et_pmids (xxx_id, numero_ligne, biblio_ligne)
FROM 'C:/Users/Public/Documents/list_utf8.csv'
DELIMITER '|'
CSV HEADER;
