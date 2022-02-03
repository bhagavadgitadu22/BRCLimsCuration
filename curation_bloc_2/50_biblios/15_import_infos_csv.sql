COPY dois_et_pmids (xxx_id, numero_ligne, biblio_ligne)
FROM 'C:/Users/Public/Documents/list_utf8.csv'
DELIMITER '|'
CSV HEADER;
