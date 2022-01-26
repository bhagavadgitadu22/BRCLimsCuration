INSERT INTO all_strains
SELECT xxx_id, sch_historique, 
unnest(string_to_array(sch_references_equi, ';')) AS strain,
unnest(string_to_array(sch_references_equi, ';')) AS short_strain
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
ORDER BY xxx_id;
