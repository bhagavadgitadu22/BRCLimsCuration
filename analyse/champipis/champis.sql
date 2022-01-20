DROP TABLE IF EXISTS souches_de_champis;

SELECT * 
INTO souches_de_champis
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 404);
