DROP TABLE IF EXISTS south_korea_places;

SELECT t_donneedico.xxx_id, don_lib, array_to_string(array_agg(sch_identifiant), ', '), city, COUNT(*) 
INTO TEMPORARY TABLE south_korea_places
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
JOIN korean_cities
ON don_lib LIKE CONCAT('%', city, '%')
WHERE don_lib NOT IN (SELECT name_en FROM world)
AND don_dic_id = 3758
AND don_lib LIKE '%Korea%'
GROUP BY t_donneedico.xxx_id, don_lib, city
ORDER BY COUNT(*) DESC;

UPDATE t_donneedico
SET don_lib = REPLACE(t_donneedico.don_lib, 'Korea', 'Korea (Republic of)')
FROM south_korea_places
WHERE t_donneedico.xxx_id = south_korea_places.xxx_id
