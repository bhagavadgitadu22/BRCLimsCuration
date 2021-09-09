-- on lit l'excel contenant les bonnes positions des lots dans le stockeur 2
DROP TABLE IF EXISTS stockeur_2;

CREATE TABLE stockeur_2 (
  first_strain varchar(75),
  last_strain varchar(75),
  balancelle varchar(75)
);

COPY stockeur_2 (first_strain, last_strain, balancelle)
FROM 'C:/Users/Public/Documents/rangement_stockeur_2.csv'
DELIMITER ';'
CSV;

UPDATE stockeur_2
SET first_strain = REPLACE(first_strain, 'A ', 'A')
WHERE first_strain LIKE '%A %';

UPDATE stockeur_2
SET last_strain = REPLACE(last_strain, 'A ', 'A')
WHERE last_strain LIKE '%A %';

UPDATE stockeur_2
SET first_strain = CONCAT('CIP ', first_strain),
	last_strain = CONCAT('CIP ', last_strain);
