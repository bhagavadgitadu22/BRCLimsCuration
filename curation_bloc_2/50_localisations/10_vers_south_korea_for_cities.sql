DROP TABLE IF EXISTS south_korea_places;

SELECT t_donneedico.xxx_id, don_lib, array_to_string(array_agg(sch_identifiant), ', '), COUNT(*) 
INTO TEMPORARY TABLE south_korea_places
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE don_dic_id = 3758
AND t_donneedico.xxx_sup_dat IS NULL
AND t_souche.xxx_sup_dat IS NULL
AND don_lib LIKE '%Korea%'
AND don_lib NOT LIKE '%Korea (Republic of)%'
GROUP BY t_donneedico.xxx_id, don_lib
ORDER BY COUNT(*) DESC;

UPDATE t_donneedico
SET don_lib = REPLACE(t_donneedico.don_lib, 'Korea', 'Korea (Republic of)')
FROM south_korea_places
WHERE t_donneedico.xxx_id = south_korea_places.xxx_id;

DROP TABLE IF EXISTS south_korea_places;
