SELECT * 
INTO TABLE t_couleurs
FROM
(SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_denomination,
t_cpr_61.cpr_com AS cp_61,
t_cpr_66.cpr_com AS cp_66

FROM t_souche

JOIN t_carac_phenotypique_resultat AS t_cpr_61
ON t_souche.xxx_id = t_cpr_61.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_61
ON t_cp_61.xxx_id = t_cpr_61.cpr_cpy_id
AND t_cp_61.cpy_numero = 61

JOIN t_carac_phenotypique_resultat AS t_cpr_66
ON t_souche.xxx_id = t_cpr_66.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_66
ON t_cp_66.xxx_id = t_cpr_66.cpr_cpy_id
AND t_cp_66.cpy_numero = 66

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND (t_cpr_61.cpr_com LIKE '%blanc%'
OR t_cpr_66.cpr_com LIKE '%blanc%')

ORDER BY sch_identifiant, sch_version DESC) AS a
ORDER BY xxx_id;

SELECT t_couleurs.xxx_id, sch_identifiant, sch_denomination,
t_cpr_60.cpr_com AS cp_60,
cp_61,
t_cpr_65.cpr_com AS cp_65,
cp_66

FROM t_couleurs
 
JOIN t_carac_phenotypique_resultat AS t_cpr_60
ON t_couleurs.xxx_id = t_cpr_60.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_60
ON t_cp_60.xxx_id = t_cpr_60.cpr_cpy_id
AND t_cp_60.cpy_numero = 60
 
JOIN t_carac_phenotypique_resultat AS t_cpr_65
ON t_couleurs.xxx_id = t_cpr_65.cpr_sch_id
LEFT JOIN t_carac_phenotypique AS t_cp_65
ON t_cp_65.xxx_id = t_cpr_65.cpr_cpy_id
AND t_cp_65.cpy_numero = 65
 
ORDER BY t_couleurs.xxx_id;