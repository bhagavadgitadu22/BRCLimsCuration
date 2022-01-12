DROP TABLE IF EXISTS unnamed_strains;

SELECT xxx_id
INTO TEMPORARY TABLE unnamed_strains
FROM t_souche 
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_denomination NOT SIMILAR TO '%[a-zA-Z]+%';

UPDATE t_souche
SET sch_denomination = 'Unnamed strain'
WHERE xxx_id IN (SELECT xxx_id FROM unnamed_strains);

DROP TABLE IF EXISTS unnamed_strains;
