SELECT t_souche.xxx_id, sch_identifiant, sch_denomination, cpr_com

FROM t_souche

LEFT JOIN t_carac_phenotypique_resultat
ON t_souche.xxx_id = cpr_sch_id
LEFT JOIN t_carac_phenotypique
ON t_carac_phenotypique.xxx_id = cpr_cpy_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_identifiant LIKE '%103181%';
