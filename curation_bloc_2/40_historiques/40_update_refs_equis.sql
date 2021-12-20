DROP TABLE IF EXISTS new_refs_equis;

SELECT xxx_id, array_to_string(ARRAY_AGG(short_strain), ';') AS ending_refs_equis
INTO TEMPORARY TABLE new_refs_equis
FROM all_strains
GROUP BY xxx_id;

UPDATE t_souche
SET sch_references_equi = CONCAT(sch_references_equi, ';', ending_refs_equis)
FROM new_refs_equis
WHERE t_souche.xxx_id = new_refs_equis.xxx_id;
