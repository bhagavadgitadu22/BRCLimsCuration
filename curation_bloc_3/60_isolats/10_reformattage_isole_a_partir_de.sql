SELECT sch_isole_a_partir_de, btrim(REGEXP_REPLACE(sch_isole_a_partir_de, E'[\\r\\n]+', '', 'g'), ' ')
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_isole_a_partir_de != ''
AND sch_isole_a_partir_de != btrim(REGEXP_REPLACE(sch_isole_a_partir_de, E'[\\r\\n]+', '', 'g'), ' ');

UPDATE t_souche
SET sch_isole_a_partir_de = btrim(REGEXP_REPLACE(sch_isole_a_partir_de, E'[\\r\\n]+', '', 'g'), ' ')
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_isole_a_partir_de != ''
AND sch_isole_a_partir_de != btrim(REGEXP_REPLACE(sch_isole_a_partir_de, E'[\\r\\n]+', '', 'g'), ' ');
