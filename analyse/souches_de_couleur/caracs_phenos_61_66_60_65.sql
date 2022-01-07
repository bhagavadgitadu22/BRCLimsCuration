DROP TABLE IF EXISTS t_couleurs;

SELECT * 
INTO TABLE t_couleurs
FROM
(SELECT DISTINCT ON (sch_identifiant) 
t_souche.xxx_id, sch_identifiant, sch_denomination,
t_cpr_61.cpr_com AS cp_61,
t_cpr_66.cpr_com AS cp_66

FROM t_souche

LEFT JOIN (SELECT t_cp_1345.xxx_id, cpr_sch_id, cpr_com
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 61) AS t_cpr_61
ON t_souche.xxx_id = t_cpr_61.cpr_sch_id

LEFT JOIN (SELECT t_cp_1345.xxx_id, cpr_sch_id, cpr_com
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 66) AS t_cpr_66
ON t_souche.xxx_id = t_cpr_66.cpr_sch_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND (t_cpr_61.cpr_com LIKE '%bleu%'
OR t_cpr_66.cpr_com LIKE '%bleu%')

ORDER BY sch_identifiant, sch_version DESC) AS a
ORDER BY xxx_id;

SELECT t_couleurs.xxx_id, sch_identifiant, sch_denomination,
t_cpr_60.cpr_resultat AS cp_60,
cp_61,
t_cpr_65.cpr_resultat AS cp_65,
cp_66

FROM t_couleurs
 
LEFT JOIN (SELECT t_cp_1345.xxx_id, cpr_sch_id, cpr_resultat
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 60) AS t_cpr_60
ON t_couleurs.xxx_id = t_cpr_60.cpr_sch_id
 
LEFT JOIN (SELECT t_cp_1345.xxx_id, cpr_sch_id, cpr_resultat
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 65) AS t_cpr_65
ON t_couleurs.xxx_id = t_cpr_65.cpr_sch_id
 
ORDER BY t_couleurs.xxx_id;