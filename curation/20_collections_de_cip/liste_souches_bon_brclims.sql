DROP TABLE IF EXISTS souches_groupe_cip;

SELECT * 
INTO souches_groupe_cip
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401);
