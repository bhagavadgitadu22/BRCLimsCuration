DROP TABLE IF EXISTS new_refs_equis_strings;

SELECT xxx_id, array_to_string(ARRAY_AGG(short_strain ORDER BY position), ';') AS new_string
INTO TABLE new_refs_equis_strings
FROM new_refs_equis
GROUP BY xxx_id;

UPDATE t_souche
SET sch_references_equi = new_string
FROM new_refs_equis_strings
WHERE t_souche.xxx_id = new_refs_equis_strings.xxx_id;
