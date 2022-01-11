SELECT EXTRACT(YEAR FROM sch_dat_acquisition), COUNT(*), ARRAY_AGG(don_lib) FILTER (WHERE don_lib IS NOT NULL) AS liste_pays
FROM 
(SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_cre_dat, sch_dat_acquisition, sch_identifiant, sch_version, don_lib
 FROM t_souche
 LEFT JOIN t_donneedico
 ON sch_lieu = t_donneedico.xxx_id
 WHERE sch_col_id IN
 (SELECT xxx_id
 FROM t_collection
 WHERE col_clg_id = 401)
 AND t_souche.xxx_sup_dat IS NULL
 ORDER BY sch_identifiant, sch_version) AS a 
WHERE EXTRACT(YEAR FROM sch_dat_acquisition) > 2013
GROUP BY EXTRACT(YEAR FROM sch_dat_acquisition)
ORDER BY EXTRACT(YEAR FROM sch_dat_acquisition) DESC;
