DROP TABLE IF EXISTS souches_bon_brc_lims;

SELECT * 
INTO souches_bon_brc_lims
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401);
