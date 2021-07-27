DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
  id SERIAL,
  city VARCHAR(75),
  city_ascii VARCHAR(75),
  lat varchar(25),
  lng varchar(25),
  country VARCHAR(75),
  iso2 varchar(25),
  iso3 varchar(25),
  admin_name varchar(75),
  capital varchar(25),
  population varchar(25),
  id_city varchar(25),
  PRIMARY KEY (id)
);

COPY cities(
	city, city_ascii, lat, lng, country, iso2, iso3, 
	admin_name, capital, population, id_city)
FROM 'C:\Users\Public\Documents\worldcities.csv'
DELIMITER ','
CSV HEADER;

ALTER TABLE cities
DROP COLUMN city, 
DROP COLUMN lat, 
DROP COLUMN lng, 
DROP COLUMN iso2, 
DROP COLUMN iso3, 
DROP COLUMN admin_name, 
DROP COLUMN capital, 
DROP COLUMN id_city;

UPDATE cities
SET population = '0'
WHERE population = '';

DELETE FROM cities AS c1
WHERE c1.population::numeric < 
(SELECT MAX(c2.population::numeric) FROM cities AS c2 
 WHERE c1.city_ascii = c2.city_ascii);