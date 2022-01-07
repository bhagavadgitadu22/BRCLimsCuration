SELECT EXTRACT(YEAR FROM sch_dat_acquisition), COUNT(*) 
FROM 
(SELECT DISTINCT ON (sch_identifiant) xxx_cre_dat, sch_dat_acquisition, sch_identifiant, sch_version
 FROM t_souche 
 WHERE sch_col_id IN
 (SELECT xxx_id
 FROM t_collection
 WHERE col_clg_id = 401)
 AND xxx_sup_dat IS NULL
 ORDER BY sch_identifiant, sch_version) AS a 
GROUP BY EXTRACT(YEAR FROM sch_dat_acquisition)
ORDER BY EXTRACT(YEAR FROM sch_dat_acquisition) DESC;
