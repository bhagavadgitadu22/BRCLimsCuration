SELECT t_origine.don_lib, sch_isole_a_partir_de
FROM t_souche
LEFT JOIN t_donneedico AS t_origine
ON t_origine.xxx_id = t_souche.sch_origine 
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip);

SELECT *
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL;

SELECT sch_isole_a_partir_de, COUNT(*)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
GROUP BY sch_isole_a_partir_de
ORDER BY COUNT(*) DESC
