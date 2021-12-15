DROP TABLE IF EXISTS korean_cities;

CREATE TABLE korean_cities (
  city varchar(75)
);

COPY korean_cities
FROM 'C:/Users/Public/Documents/south_korean_cities.csv'
DELIMITER ';'
CSV HEADER;

UPDATE korean_cities
SET city = REPLACE(city, 'County', '');

UPDATE korean_cities
SET city = TRIM(city);

DELETE FROM korean_cities
WHERE city IS NULL;

SELECT * FROM korean_cities;
