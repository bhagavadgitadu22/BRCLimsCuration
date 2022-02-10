DROP TABLE IF EXISTS origine_plante;
DROP TABLE IF EXISTS nombre_plante;

SELECT xxx_id, sch_isole_a_partir_de, btrim(REGEXP_REPLACE(sch_isole_a_partir_de, '(P|p)lant[es]*', ''), ', ()') AS new_isole
INTO TABLE origine_plante
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) LIKE 'plant%';

SELECT DISTINCT t_donneedico.xxx_id 
INTO TABLE nombre_plante
FROM t_donneedico
JOIN t_souche
ON sch_origine = t_donneedico.xxx_id
WHERE don_lib = 'Plant';

/*
SELECT (SELECT xxx_id FROM nombre_plante), CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM t_souche
JOIN origine_plante
ON t_souche.xxx_id = origine_plante.xxx_id;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_plante),
	sch_isole_a_partir_de = CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM origine_plante
WHERE t_souche.xxx_id = origine_plante.xxx_id;
