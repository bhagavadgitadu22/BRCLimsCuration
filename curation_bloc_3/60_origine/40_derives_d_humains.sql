/*
SELECT sch_isole_a_partir_de, (SELECT category FROM nombre_humain)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(child|newborn|infant)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%wall%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_humain)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(child|newborn|infant)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%wall%';
