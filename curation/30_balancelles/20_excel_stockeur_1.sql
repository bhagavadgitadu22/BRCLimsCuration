-- on lit l'excel contenant les bonnes positions des lots dans le stockeur 1
DROP TABLE IF EXISTS stockeur_1;

CREATE TABLE stockeur_1 (
  first_strain varchar(75),
  last_strain varchar(75),
  balancelle varchar(75)
);

COPY stockeur_1 (first_strain, last_strain, balancelle)
FROM '/var/lib/pgsql/brclimscuration/csv_utiles/rangement_stockeur_1.csv'
DELIMITER ';'
CSV;

UPDATE stockeur_1
SET first_strain = REPLACE(first_strain, 'A ', 'A')
WHERE first_strain LIKE '%A %';

UPDATE stockeur_1
SET last_strain = REPLACE(last_strain, 'A ', 'A')
WHERE last_strain LIKE '%A %';

UPDATE stockeur_1
SET first_strain = CONCAT('CIP ', first_strain),
	last_strain = CONCAT('CIP ', last_strain);
