-- on mixe les tables des pays en anglais et français
DROP TABLE IF EXISTS world;

CREATE TABLE world (
  id int NOT NULL,
  name_en varchar(75) NOT NULL DEFAULT '',
  name_fr varchar(75) NOT NULL DEFAULT '',
  PRIMARY KEY (id)
);

INSERT INTO world
SELECT world_en.id, world_en.name AS name_en, world_fr.name AS name_fr
FROM world_en
JOIN world_fr ON world_en.id = world_fr.id;

ALTER TABLE world 
DROP COLUMN id;
