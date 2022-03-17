DROP TABLE IF EXISTS origine_food;
DROP TABLE IF EXISTS nombre_food;

SELECT xxx_id, sch_isole_a_partir_de, btrim(REGEXP_REPLACE(sch_isole_a_partir_de, '(F|f)ood(?=([^A-Za-z]+|$))', ''), ', *:.-') AS new_isole
INTO TABLE origine_food
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO 'food%';

SELECT DISTINCT t_donneedico.xxx_id , 'Food' AS category
INTO TABLE nombre_food
FROM t_donneedico
JOIN t_souche
ON sch_origine = t_donneedico.xxx_id
WHERE don_lib = 'Food';

/*
SELECT (SELECT category FROM nombre_food), CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM t_souche
JOIN origine_food
ON t_souche.xxx_id = origine_food.xxx_id;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_food),
	sch_isole_a_partir_de = CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM origine_food
WHERE t_souche.xxx_id = origine_food.xxx_id;

