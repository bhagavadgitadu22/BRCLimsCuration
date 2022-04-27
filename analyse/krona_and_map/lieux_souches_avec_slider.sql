SELECT array_to_string(array_agg(CONCAT(year, ':', compte)), '|'), don_lib
FROM
(SELECT EXTRACT(YEAR FROM sch_dat_isolement) AS year, COUNT(*) AS compte, don_lib
FROM t_souche
JOIN t_donneedico
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY don_lib, EXTRACT(YEAR FROM sch_dat_isolement)
ORDER BY don_lib, EXTRACT(YEAR FROM sch_dat_isolement)) AS a
GROUP BY don_lib;
