CREATE EXTENSION IF NOT EXISTS unaccent;

-- on fait gaffe aux problèmes d'accent et de majuscules
UPDATE t_donneedico
SET don_lib = name_en
FROM world
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND LOWER(unaccent(don_lib)) = LOWER(unaccent(name_en))
AND don_lib != name_en;

UPDATE t_donneedico
SET don_lib = name_en
FROM world
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND LOWER(unaccent(don_lib)) = LOWER(unaccent(name_fr))
AND don_lib != name_fr;

-- de même pour les villes
UPDATE t_donneedico
SET don_lib = city_ascii
FROM world_cities
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND LOWER(unaccent(don_lib)) = LOWER(unaccent(city_ascii))
AND don_lib != city_ascii;
