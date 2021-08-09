SELECT id_lieu, don_lib, city_ascii, country

FROM (SELECT t_donneedico.xxx_id AS id_lieu, don_lib
FROM t_donneedico
INNER JOIN t_souche 
ON t_donneedico.xxx_id = t_souche.sch_lieu
GROUP BY t_donneedico.xxx_id) AS lieux

JOIN cities
ON lieux.don_lib SIMILAR TO CONCAT('%([^A-Za-z0-9]+|$)', cities.city_ascii, '([^A-Za-z0-9]+|$)%')
WHERE cities.city_ascii NOT IN (SELECT name_en FROM world) AND cities.city_ascii != cities.country;