/*
SELECT xxx_id, sch_isole_a_partir_de
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%water%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(skin|fish|dolphin|halibut)%';
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_environnement)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%water%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(skin|fish|dolphin|halibut)%';
