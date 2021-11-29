SELECT cpr_resultat
FROM t_souche
JOIN t_carac_phenotypique_resultat
ON t_souche.xxx_id = cpr_sch_id
JOIN t_carac_phenotypique 
ON t_carac_phenotypique.xxx_id = cpr_cpy_id
WHERE cpy_numero = 1546