DROP TABLE IF EXISTS origine_humaine;
DROP TABLE IF EXISTS nombre_humain;

SELECT xxx_id, sch_isole_a_partir_de, btrim(REGEXP_REPLACE(sch_isole_a_partir_de, '(H|h)uman', ''), ', ()') AS new_isole
INTO TABLE origine_humaine
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) LIKE 'human%';

SELECT DISTINCT t_donneedico.xxx_id 
INTO TABLE nombre_humain
FROM t_donneedico
JOIN t_souche
ON sch_origine = t_donneedico.xxx_id
WHERE don_lib = 'Human';

/*
SELECT (SELECT xxx_id FROM nombre_humain), CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM t_souche
JOIN origine_humaine
ON t_souche.xxx_id = origine_humaine.xxx_id;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_humain),
	sch_isole_a_partir_de = CONCAT(UPPER(LEFT(new_isole, 1)), RIGHT(new_isole, -1))
FROM origine_humaine
WHERE t_souche.xxx_id = origine_humaine.xxx_id;
