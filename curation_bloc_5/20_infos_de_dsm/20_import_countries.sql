COPY dsm_countries (identifier, country, precision)
FROM '/csv/20_infos_de_dsm/list_countries_utf8.csv'
DELIMITER ';';
