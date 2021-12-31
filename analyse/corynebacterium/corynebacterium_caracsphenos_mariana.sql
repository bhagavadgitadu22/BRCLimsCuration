SELECT * FROM
(SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_id,

t_cpr_1345.cpr_resultat AS cp_1345,
t_cpr_1346.cpr_resultat AS cp_1346,
t_cpr_1517.cpr_resultat AS cp_1517,
t_cpr_1531.cpr_resultat AS cp_1531,
t_cpr_1546.cpr_resultat AS cp_1546

FROM t_souche

LEFT JOIN t_carac_phenotypique_resultat AS t_cpr_1345
ON t_souche.xxx_id = t_cpr_1345.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 1345

LEFT JOIN t_carac_phenotypique_resultat AS t_cpr_1346
ON t_souche.xxx_id = t_cpr_1346.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_1346
ON t_cp_1346.xxx_id = t_cpr_1346.cpr_cpy_id
AND t_cp_1346.cpy_numero = 1346

LEFT JOIN t_carac_phenotypique_resultat AS t_cpr_1517
ON t_souche.xxx_id = t_cpr_1517.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_1517
ON t_cp_1517.xxx_id = t_cpr_1517.cpr_cpy_id
AND t_cp_1517.cpy_numero = 1517

LEFT JOIN t_carac_phenotypique_resultat AS t_cpr_1531
ON t_souche.xxx_id = t_cpr_1531.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_1531
ON t_cp_1531.xxx_id = t_cpr_1531.cpr_cpy_id
AND t_cp_1531.cpy_numero = 1531

LEFT JOIN t_carac_phenotypique_resultat AS t_cpr_1546
ON t_souche.xxx_id = t_cpr_1546.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_1546
ON t_cp_1546.xxx_id = t_cpr_1546.cpr_cpy_id
AND t_cp_1546.cpy_numero = 1546

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM t_souche)
AND sch_denomination LIKE 'Corynebacterium%'

ORDER BY sch_identifiant, sch_version DESC) AS a
ORDER BY xxx_id;