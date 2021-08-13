DROP TABLE IF EXISTS world_cities;

CREATE TABLE world_cities (
  id SERIAL,
  ascii_name VARCHAR(75),
  country_name VARCHAR(75),
  population VARCHAR(75),
  PRIMARY KEY (id)
);

COPY world_cities(ascii_name, country_name, population)
FROM 'C:\Users\Public\Documents\geonames_cities_simplified2.csv'
DELIMITER ';'
CSV HEADER;
