DROP TABLE IF EXISTS origine_human;

SELECT last_version_souches_cip.xxx_id, don_lib, sch_isole_a_partir_de, REPLACE(sch_isole_a_partir_de, 'Human, ', '') AS new_isole
INTO origine_human
FROM last_version_souches_cip
LEFT JOIN t_donneedico 
ON sch_origine = t_donneedico.xxx_id
WHERE sch_isole_a_partir_de SIMILAR TO 'Human, %';

/*
SELECT t_souche.sch_isole_a_partir_de, CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM t_souche
JOIN origine_human
ON t_souche.xxx_id = origine_human.xxx_id;
*/

UPDATE t_souche
SET sch_isole_a_partir_de = CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM origine_human
WHERE t_souche.xxx_id = origine_human.xxx_id;
