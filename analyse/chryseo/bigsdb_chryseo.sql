SELECT sch_identifiant, sch_references_equi, '', EXTRACT(YEAR FROM sch_dat_isolement), t_origine.don_lib, 
sch_isole_a_partir_de, t_lieu.don_lib, sch_lieu_precis, '', '', '', 
CONCAT((string_to_array(sch_denomination, ' '))[1], ' ', (string_to_array(sch_denomination, ' '))[2]), 
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS subspecies, '', 
CASE
	WHEN sch_type IS TRUE THEN 'yes'
	ELSE 'no'
END AS subspecies,
'P2M'
FROM t_souche
LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id
LEFT JOIN t_donneedico AS t_origine
ON sch_origine = t_origine.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND (sch_identifiant IN (SELECT souche FROM souches_chryseos)
	 OR sch_identifiant IN (SELECT CONCAT(souche, 'T') FROM souches_chryseos))