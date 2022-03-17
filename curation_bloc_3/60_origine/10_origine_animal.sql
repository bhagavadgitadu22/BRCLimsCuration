DROP TABLE IF EXISTS origine_animal;
DROP TABLE IF EXISTS nombre_animal;

SELECT xxx_id, sch_isole_a_partir_de, btrim(REGEXP_REPLACE(sch_isole_a_partir_de, '(A|a)nimal(?=([^A-Za-z]+|$))', ''), ', *:.-') AS new_isole
INTO TABLE origine_animal
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO 'animal%';

SELECT DISTINCT t_donneedico.xxx_id, 'Animal' AS category
INTO TABLE nombre_animal
FROM t_donneedico
JOIN t_souche
ON sch_origine = t_donneedico.xxx_id
WHERE don_lib = 'Animal';

/*
SELECT (SELECT category FROM nombre_animal), CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM t_souche
JOIN origine_animal
ON t_souche.xxx_id = origine_animal.xxx_id;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal),
	sch_isole_a_partir_de = CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM origine_animal
WHERE t_souche.xxx_id = origine_animal.xxx_id;

