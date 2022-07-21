SELECT don_lib, COUNT(*), array_to_string(ARRAY_AGG(sch_identifiant), ', ')
FROM t_souche
JOIN t_donneedico
ON t_donneedico.xxx_id = sch_lieu
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
GROUP BY don_lib
ORDER BY don_lib;
