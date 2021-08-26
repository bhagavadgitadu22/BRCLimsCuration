DROP TABLE IF EXISTS stockeur_1;

CREATE TABLE stockeur_1 (
  first_strain varchar(75),
  last_strain varchar(75),
  balancelle varchar(75),
  id_first_strain int,
  id_last_strain int
);

COPY stockeur_1 (first_strain, last_strain, balancelle)
FROM 'C:/Users/Public/Documents/rangement_stockeur_1.csv'
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
	
UPDATE stockeur_1
SET id_first_strain = id
FROM souches_triees
WHERE stockeur_1.first_strain = souches_triees.sch_identifiant;

UPDATE stockeur_1
SET id_last_strain = id
FROM souches_triees
WHERE stockeur_1.last_strain = souches_triees.sch_identifiant;
