UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, '–', '-')
WHERE sch_bibliographie LIKE '%–%';

DROP TABLE IF EXISTS biblios_a_casser;

CREATE TABLE biblios_a_casser (
  string_doc varchar(200),
  new_string varchar(200)
);

COPY biblios_a_casser
FROM 'C:/Users/Public/Documents/separation_biblios_utf8.csv'
DELIMITER '|'
CSV;

UPDATE t_souche
SET sch_bibliographie = REPLACE(
	sch_bibliographie, 
	string_doc, 
	new_string
)
FROM biblios_a_casser
WHERE sch_bibliographie LIKE CONCAT('%', string_doc, '%');
