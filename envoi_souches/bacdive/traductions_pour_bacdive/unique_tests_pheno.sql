SELECT don_lib, ARRAY_AGG(DISTINCT t_donneedico.xxx_id)
FROM t_souche_t_carac_phenotypique_resultat
JOIN t_souche
ON strainentity_xxx_id = t_souche.xxx_id
JOIN t_carac_phenotypique_resultat
ON phenotypiccaracteristicresult_xxx_id = t_carac_phenotypique_resultat.xxx_id
JOIN t_carac_phenotypique
ON t_carac_phenotypique.xxx_id = cpr_cpy_id
JOIN t_donneedico
ON cpy_id = t_donneedico.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
AND don_lib SIMILAR TO '%[a-zA-Z]+%'
GROUP BY don_lib
ORDER BY don_lib;