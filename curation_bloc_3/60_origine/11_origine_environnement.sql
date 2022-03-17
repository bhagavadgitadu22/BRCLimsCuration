DROP TABLE IF EXISTS origine_environnement;
DROP TABLE IF EXISTS nombre_environnement;

SELECT xxx_id, sch_isole_a_partir_de, btrim(REGEXP_REPLACE(sch_isole_a_partir_de, '(E|e)nvironment(?=([^A-Za-z]+|$))', ''), ', *:.-') AS new_isole
INTO TABLE origine_environnement
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO 'environment%';

SELECT DISTINCT t_donneedico.xxx_id, 'Environment' AS category
INTO TABLE nombre_environnement
FROM t_donneedico
JOIN t_souche
ON sch_origine = t_donneedico.xxx_id
WHERE don_lib = 'Environment';

/*
SELECT (SELECT category FROM nombre_environnement), CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM t_souche
JOIN origine_environnement
ON t_souche.xxx_id = origine_environnement.xxx_id;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_environnement),
	sch_isole_a_partir_de = CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM origine_environnement
WHERE t_souche.xxx_id = origine_environnement.xxx_id;

