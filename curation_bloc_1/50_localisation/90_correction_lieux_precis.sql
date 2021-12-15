DROP TABLE IF EXISTS point_virgule_en_trop;

SELECT * 
INTO TEMPORARY TABLE point_virgule_en_trop
FROM 
(SELECT sch_identifiant, sch_lieu_precis,
TRIM(substring(sch_lieu_precis, '^(.*);')) AS beginning_str,
TRIM(substring(sch_lieu_precis, '[^;]*$')) AS end_str
FROM t_souche 
WHERE sch_lieu_precis LIKE '%;%') AS a
WHERE beginning_str LIKE CONCAT('%', end_str, '%');

UPDATE t_souche
SET sch_lieu_precis = beginning_str
FROM point_virgule_en_trop
WHERE t_souche.sch_identifiant = point_virgule_en_trop.sch_identifiant;

DROP TABLE IF EXISTS point_virgule_en_trop;

SELECT * 
INTO TEMPORARY TABLE point_virgule_en_trop
FROM 
(SELECT sch_identifiant, sch_lieu_precis,
TRIM(substring(sch_lieu_precis, '^(.*);')) AS beginning_str,
TRIM(substring(sch_lieu_precis, '[^;]*$')) AS end_str
FROM t_souche 
WHERE sch_lieu_precis LIKE '%;%') AS a
WHERE end_str LIKE CONCAT('%', beginning_str, '%');

UPDATE t_souche
SET sch_lieu_precis = end_str
FROM point_virgule_en_trop
WHERE t_souche.sch_identifiant = point_virgule_en_trop.sch_identifiant;

DROP TABLE IF EXISTS point_virgule_en_trop;
