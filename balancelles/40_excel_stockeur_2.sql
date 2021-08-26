DROP TABLE IF EXISTS stockeur_2;

CREATE TABLE stockeur_2 (
  first_strain varchar(75),
  last_strain varchar(75),
  balancelle varchar(75),
  id_first_strain int,
  id_last_strain int
);

COPY stockeur_2 (first_strain, last_strain, balancelle)
FROM 'C:/Users/Public/Documents/rangement_stockeur_2.csv'
DELIMITER ';'
CSV;

UPDATE stockeur_2
SET first_strain = CONCAT('CIP ', first_strain),
	last_strain = CONCAT('CIP ', last_strain);
	
UPDATE stockeur_2
SET id_first_strain = id
FROM souches_triees
WHERE stockeur_2.first_strain = souches_triees.sch_identifiant;

UPDATE stockeur_2
SET id_last_strain = id
FROM souches_triees
WHERE stockeur_2.last_strain = souches_triees.sch_identifiant;
