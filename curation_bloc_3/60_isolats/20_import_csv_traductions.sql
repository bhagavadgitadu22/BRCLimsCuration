DROP TABLE IF EXISTS isole_a_partir_de_traduits;

CREATE TABLE isole_a_partir_de_traduits (
	new_isolat text, 
	old_isolate text,
	xxx_id integer
);

COPY isole_a_partir_de_traduits (new_isolat, old_isolate, xxx_id)
FROM 'C:/Users/Public/Documents/isole_a_partir_de_traduits_eclates.csv'
DELIMITER '|' CSV;
