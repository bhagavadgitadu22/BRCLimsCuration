UPDATE t_souche
SET sch_lieu = (SELECT xxx_id FROM t_donneedico WHERE don_lib = 'Korea (Republic of)' AND don_dic_id = 3758 LIMIT 1)
FROM t_donneedico
WHERE sch_lieu = t_donneedico.xxx_id
AND don_lib = 'Korea'
AND don_dic_id = 3758
AND sch_dat_isolement > TO_TIMESTAMP(1960);

DROP TABLE IF EXISTS korean_cities;
DROP TABLE IF EXISTS south_korea_places;
