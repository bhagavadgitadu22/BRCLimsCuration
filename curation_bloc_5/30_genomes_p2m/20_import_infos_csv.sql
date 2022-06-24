COPY infos_p2m (identifiant, lot, p2m, date)
FROM '/csv/30_genomes_p2m/infos_de_p2m_utf8.csv'
DELIMITER ';';

UPDATE infos_p2m
SET identifiant = TRIM(REGEXP_REPLACE(REPLACE(REPLACE(REPLACE(identifiant, 'CIP', 'CIP '), '-', '.'), 'T', ''), '(CIP|CRBIP) ?', ''));

DELETE
FROM infos_p2m
WHERE p2m = '' OR p2m NOT SIMILAR TO '(16|17)%';
