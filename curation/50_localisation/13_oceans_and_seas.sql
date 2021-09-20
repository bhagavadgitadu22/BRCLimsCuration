-- on ajoute au mix les mers, les océans et les continents
COPY world (name_en)
FROM '/var/lib/pgsql/brclimscuration/csv_utiles/complete_seas_and_oceans.csv'
DELIMITER ';';

INSERT INTO world (name_en) VALUES
('Africa'), 
('Asia'), 
('North America'), 
('South America'), 
('Europe'),
('Space'),
('Unknown'),
('Arctic');
