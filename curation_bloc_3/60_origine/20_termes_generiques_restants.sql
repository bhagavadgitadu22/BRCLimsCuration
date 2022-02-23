/*
SELECT xxx_id, sch_isole_a_partir_de, (SELECT category FROM nombre_animal)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%animal%'
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(pig|intestines|adult)%';
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%animal%'
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(pig|intestines|adult)%';

/*
SELECT xxx_id, sch_isole_a_partir_de, (SELECT category FROM nombre_environnement)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%environ(ne)?ment%';
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_environnement)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%environ(ne)?ment%';

/*
SELECT xxx_id, sch_isole_a_partir_de, (SELECT category FROM nombre_food)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%food%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(non-food|room|plant?|ecological|fed)%';
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_food)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%food%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(non-food|room|plant?|ecological|fed)%';

/*
SELECT xxx_id, sch_isole_a_partir_de, (SELECT category FROM nombre_humain)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%humai?n%';
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_humain)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%humai?n%';

-- je ne m occupe pas de plant car ambiguite usine/plante embetante a gerer
/*
SELECT sch_isole_a_partir_de, (SELECT category FROM nombre_plante)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(tea|corn|cotton|nitrogen-fixing|host|pea|poaceae|gentian|blueberry|pollinated|sesame|cucumber|composting) plant%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_plante)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(tea|corn|cotton|nitrogen-fixing|host|pea|poaceae|gentian|blueberry|pollinated|sesame|cucumber|composting) plant%';
