SELECT COUNT(*), don_lib
FROM t_souche
JOIN t_donneedico
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY don_lib;

SELECT don_lib, sch_lieu_precis, sch_dat_isolement
FROM t_souche
JOIN t_donneedico
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False;
