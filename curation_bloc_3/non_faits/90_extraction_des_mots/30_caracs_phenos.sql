SELECT t_souche.xxx_id, cpy_numero, don_lib, cpy_methode, cpr_resultat, cpr_com

FROM t_souche
JOIN t_souche_t_carac_phenotypique_resultat
ON t_souche.xxx_id = strainentity_xxx_id
JOIN t_carac_phenotypique_resultat AS t_cpr
ON phenotypiccaracteristicresult_xxx_id = t_cpr.xxx_id
JOIN t_carac_phenotypique AS t_cp
ON t_cp.xxx_id = cpr_cpy_id
JOIN t_donneedico
ON cpy_id = t_donneedico.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM ids_mots)
ORDER BY xxx_id;
