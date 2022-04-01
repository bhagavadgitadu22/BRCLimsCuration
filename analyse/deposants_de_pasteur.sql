SELECT don_lib, COUNT(*)
FROM last_version_souches_cip 
JOIN t_donneedico
ON sch_depositaire = t_donneedico.xxx_id
WHERE sch_catalogue IS True
AND LOWER(don_lib) LIKE '%pasteur%'
GROUP BY don_lib
ORDER BY COUNT(*) DESC;
