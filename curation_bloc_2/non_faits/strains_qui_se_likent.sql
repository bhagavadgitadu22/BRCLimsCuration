DROP TABLE IF EXISTS all_strains;

SELECT xxx_id, sch_references_equi, 
unnest(string_to_array(sch_references_equi, ';')) AS short_strain
INTO TABLE all_strains
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
ORDER BY xxx_id;

SELECT * 
FROM all_strains

