SELECT cpy_numero, don_lib, cpy_methode, cpr_resultat, ARRAY_AGG(sch_identifiant), ARRAY_AGG(cpr_com)
FROM t_souche
JOIN t_carac_phenotypique_resultat
ON t_souche.xxx_id = cpr_sch_id
JOIN t_carac_phenotypique 
ON t_carac_phenotypique.xxx_id = cpr_cpy_id
JOIN t_donneedico
ON cpy_id = t_donneedico.xxx_id
--WHERE cpy_numero = 21
GROUP BY cpy_numero, don_lib, cpy_methode, cpr_resultat
ORDER BY cpy_numero;
