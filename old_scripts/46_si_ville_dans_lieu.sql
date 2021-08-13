SELECT xxx_id, don_lib, city_ascii, country
FROM t_donneedico
JOIN world_cities
ON don_lib SIMILAR TO CONCAT('%([^A-Za-z0-9]+|$)', world_cities.city_ascii, '([^A-Za-z0-9]+|$)%')
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND world_cities.city_ascii NOT IN (SELECT name_en FROM world) AND world_cities.city_ascii != world_cities.country;