SELECT * FROM (SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_id,
CASE WHEN t_pheno.xxx_id IS NULL THEN 'N'
	ELSE 'Y'
END AS antibiogrammes, t_pheno.cpr_resultat

FROM t_souche

LEFT JOIN (SELECT t_cp_1345.xxx_id, cpr_resultat, cpr_sch_id
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 1546) AS t_pheno
ON t_souche.xxx_id = t_pheno.cpr_sch_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM t_souche)
AND sch_denomination LIKE 'Corynebacterium%'

ORDER BY sch_identifiant, sch_version DESC) AS a
ORDER BY xxx_id;