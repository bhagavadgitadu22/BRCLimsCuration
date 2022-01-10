DROP TABLE IF EXISTS t_couleurs;

SELECT * 
INTO TABLE t_couleurs
FROM
(SELECT sch_identifiant, array_to_string(ARRAY_AGG(DISTINCT sch_denomination) FILTER (WHERE sch_denomination IS NOT NULL), E'\n') AS sch_denomination,
array_to_string(ARRAY_AGG(DISTINCT t_cpr_61.cpr_com) FILTER (WHERE t_cpr_61.cpr_com IS NOT NULL), E'\n') AS cp_61,
array_to_string(ARRAY_AGG(DISTINCT t_cpr_66.cpr_com) FILTER (WHERE t_cpr_66.cpr_com IS NOT NULL), E'\n') AS cp_66

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
AND (t_cpr_61.cpr_com LIKE '%noir%'
OR t_cpr_66.cpr_com LIKE '%noir%')

GROUP BY sch_identifiant) AS a;

SELECT t_couleurs.sch_identifiant, t_couleurs.sch_denomination,
array_to_string(ARRAY_AGG(DISTINCT t_cpr_60.cpr_resultat) FILTER (WHERE t_cpr_60.cpr_resultat IS NOT NULL), E'\n') AS cp_60,
cp_61,
array_to_string(ARRAY_AGG(DISTINCT t_cpr_65.cpr_resultat) FILTER (WHERE t_cpr_65.cpr_resultat IS NOT NULL), E'\n') AS cp_65,
cp_66

FROM t_couleurs
 
LEFT JOIN (SELECT t_souche.sch_identifiant, t_cp_1345.xxx_id, cpr_resultat
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 60
JOIN t_souche
ON cpr_sch_id = t_souche.xxx_id) AS t_cpr_60
ON t_couleurs.sch_identifiant = t_cpr_60.sch_identifiant
 
LEFT JOIN (SELECT t_souche.sch_identifiant, t_cp_1345.xxx_id, cpr_resultat
FROM t_carac_phenotypique_resultat AS t_cpr_1345
JOIN t_carac_phenotypique AS t_cp_1345
ON t_cp_1345.xxx_id = t_cpr_1345.cpr_cpy_id
AND t_cp_1345.cpy_numero = 65
JOIN t_souche
ON cpr_sch_id = t_souche.xxx_id) AS t_cpr_65
ON t_couleurs.sch_identifiant = t_cpr_65.sch_identifiant

GROUP BY t_couleurs.sch_identifiant, t_couleurs.sch_denomination, cp_61, cp_66
ORDER BY t_couleurs.sch_identifiant;