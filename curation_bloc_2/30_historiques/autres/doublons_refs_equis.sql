DROP TABLE IF EXISTS doublons;

SELECT xxx_id, unnest(string_to_array(sch_references_equi, ';')) AS repet, sch_references_equi
INTO TEMPORARY TABLE doublons
FROM t_souche 
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
GROUP BY xxx_id, unnest(string_to_array(sch_references_equi, ';'))
HAVING COUNT(*) > 1;

SELECT t_souche.sch_references_equi, REGEXP_REPLACE(t_souche.sch_references_equi, CONCAT('(?<=', repet, '.*);', repet), '', 'g')
FROM t_souche
JOIN doublons
ON t_souche.xxx_id = doublons.xxx_id;

/*
UPDATE t_souche
SET sch_references_equi = REGEXP_REPLACE(CONCAT('(?<=', repet, '.*)', repet), '', 'g')
FROM doublons
WHERE t_souche.xxx_id = doublons.xxx_id;
*/
