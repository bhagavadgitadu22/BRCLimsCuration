SELECT * FROM
(SELECT ARRAY_REMOVE(ARRAY_AGG(DISTINCT t_origine.don_lib), NULL) AS arr, 
sch_isole_a_partir_de, COUNT(*) AS count
FROM t_souche
LEFT JOIN t_donneedico AS t_origine
ON t_origine.xxx_id = t_souche.sch_origine 
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
GROUP BY sch_isole_a_partir_de) AS a
WHERE array_length(arr, 1) = 1
ORDER BY arr, -count;
