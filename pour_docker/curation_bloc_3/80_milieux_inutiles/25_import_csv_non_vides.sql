COPY milieux_non_vides (numero, remplacant)
FROM '/csv/80_milieux_inutiles/milieux_non_vides.csv'
DELIMITER ';' CSV HEADER;
