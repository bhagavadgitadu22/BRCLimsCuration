SELECT * 
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False;

SELECT (string_to_array(sch_denomination, ' '))[1] AS genus, (string_to_array(sch_denomination, ' '))[2] AS species
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY (string_to_array(sch_denomination, ' '))[1], (string_to_array(sch_denomination, ' '))[2];

-- countries checked with my python program to do the geojson

SELECT * 
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
AND sch_type IS True;

SELECT * FROM
(SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_id,
t_cpr_1546.cpr_resultat, t_cpr_1546.cpr_com
 
FROM t_souche
 
JOIN t_carac_phenotypique_resultat AS t_cpr_1546
ON t_souche.xxx_id = t_cpr_1546.cpr_sch_id
JOIN t_carac_phenotypique AS t_cp_1546
ON t_cp_1546.xxx_id = t_cpr_1546.cpr_cpy_id
AND t_cp_1546.cpy_numero = 1546

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False

ORDER BY sch_identifiant, sch_version DESC) AS a
ORDER BY xxx_id;
