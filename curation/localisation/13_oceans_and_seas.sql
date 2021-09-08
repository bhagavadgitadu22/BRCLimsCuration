COPY world (name_en)
FROM 'C:\Users\Public\Documents\complete_seas_and_oceans.csv'
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

