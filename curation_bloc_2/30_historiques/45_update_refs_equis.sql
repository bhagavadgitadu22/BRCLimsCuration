DROP TABLE IF EXISTS new_refs_equis;

SELECT xxx_id, array_to_string(ARRAY_AGG(short_strain ORDER BY position), ';') AS new_string
INTO TABLE new_refs_equis
FROM all_strains_grouped
GROUP BY xxx_id;

UPDATE t_souche
SET sch_references_equi = new_string
FROM new_refs_equis
WHERE t_souche.xxx_id = new_refs_equis.xxx_id;
