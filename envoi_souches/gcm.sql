SELECT sch_identifiant, sch_references_equi, 
(string_to_array(sch_denomination, ' '))[1] AS genus, (string_to_array(sch_denomination, ' '))[2] AS species,
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS subspecies, '', 'Bacteria', 
sch_historique, sch_dat_isolement, sch_isole_a_partir_de, 
t_lieu.don_lib, 
CASE
	WHEN sch_type IS True THEN 'Type'
	ELSE ''
END AS statut, sch_temperature_incubation, 
array_to_string(ARRAY_AGG(CONCAT('CIP ', mil_designation_en)), ' ; '),
'', sch_bibliographie, CONCAT('https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=', sch_identifiant) AS original_site
FROM t_souche
LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id
LEFT JOIN t_milieu_souche
ON t_souche.xxx_id = msc_sch_id
LEFT JOIN t_milieu
ON msc_mil_id = t_milieu.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY sch_identifiant, sch_references_equi, sch_denomination, sch_historique, sch_dat_isolement, 
sch_isole_a_partir_de, t_lieu.don_lib, sch_type, sch_temperature_incubation, sch_bibliographie;

/*
SELECT sch_identifiant, sch_denomination, 
(string_to_array(sch_denomination, ' '))[1], 
(string_to_array(sch_denomination, ' '))[2],
(string_to_array(sch_denomination, ' '))[3],
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
AND (string_to_array(sch_denomination, ' '))[3] IS NOT NULL;
*/
