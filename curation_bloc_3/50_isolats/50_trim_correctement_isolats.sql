/*
SELECT sch_isole_a_partir_de, btrim(regexp_replace(sch_isole_a_partir_de, E'[\\t]+', ''), '* ')
FROM t_souche
WHERE sch_isole_a_partir_de != ''
AND sch_isole_a_partir_de NOT SIMILAR TO '[A-Z]{1}%';
--GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_isole_a_partir_de = btrim(regexp_replace(sch_isole_a_partir_de, E'[\\t]+', ''), '* ')
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_isole_a_partir_de != btrim(regexp_replace(sch_isole_a_partir_de, E'[\\t]+', ''), '* ');

UPDATE t_souche
SET sch_isole_a_partir_de = CONCAT(UPPER(LEFT(sch_isole_a_partir_de, 1)), RIGHT(sch_isole_a_partir_de, -1))
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_isole_a_partir_de SIMILAR TO '[a-z]{1}%';

UPDATE t_souche
SET sch_isole_a_partir_de = CONCAT(LEFT(sch_isole_a_partir_de, -1), ' days')
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_isole_a_partir_de SIMILAR TO 'Ducklings [0-9]+j';

UPDATE t_souche
SET sch_isole_a_partir_de = CONCAT(LEFT(sch_isole_a_partir_de, -1), ' weeks')
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_isole_a_partir_de SIMILAR TO 'Ducklings B. [0-9]+s';
