SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_isole_a_partir_de, sch_isole_a_partir_de
FROM t_souche
LEFT JOIN t_donneedico
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND t_donneedico.xxx_id IS NULL
AND (LOWER(sch_isole_a_partir_de) LIKE ANY(SELECT CONCAT('%', LOWER(name_en), '%') FROM world WHERE name_en != '')
	 OR LOWER(sch_isole_a_partir_de) LIKE ANY(SELECT CONCAT('%', LOWER(name_fr), '%') FROM world WHERE name_fr != ''))
ORDER BY sch_isole_a_partir_de;
