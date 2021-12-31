SELECT sch_denomination, array_to_string(ARRAY_AGG(DISTINCT sch_identifiant), E'\n'), COUNT(DISTINCT sch_identifiant)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_denomination SIMILAR TO '%[a-zA-Z]+%'
GROUP BY sch_denomination
ORDER BY COUNT(DISTINCT sch_identifiant) DESC;
