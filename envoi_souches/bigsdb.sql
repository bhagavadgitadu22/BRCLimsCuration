SELECT sch_identifiant, sch_references_equi, t_lieu.don_lib, 
sch_lieu_precis,
EXTRACT(YEAR FROM sch_dat_isolement), sch_isole_a_partir_de,
(string_to_array(sch_denomination, ' '))[2] AS species,
(string_to_array(sch_denomination, ' '))[1] AS genus, 
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS subspecies,
sch_type
FROM t_souche
LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)