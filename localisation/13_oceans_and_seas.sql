COPY world (name_en)
FROM 'C:\Users\Public\Documents\complete_seas_and_oceans.csv'
DELIMITER ';';

INSERT INTO world (name_en) VALUES
('Space');