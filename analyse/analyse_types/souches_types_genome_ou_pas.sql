SELECT sch_identifiant, 
CASE WHEN t_1546.xxx_id IS NULL THEN 'N'
	ELSE 'Y'
END AS genome,
t_1546.cpr_com
FROM last_version_souches_cip

LEFT JOIN (SELECT t_cp.xxx_id, cpr_sch_id, cpr_com
FROM t_carac_phenotypique_resultat AS t_cpr
JOIN t_carac_phenotypique AS t_cp
ON t_cp.xxx_id = t_cpr.cpr_cpy_id
AND t_cp.cpy_numero = 1546) AS t_1546
ON last_version_souches_cip.xxx_id = t_1546.cpr_sch_id

WHERE sch_type IS True
AND sch_catalogue IS NOT True
ORDER BY sch_identifiant;
