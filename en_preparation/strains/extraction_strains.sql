SELECT xxx_id, sch_references_equi, sch_historique,
strain
FROM 

(SELECT xxx_id, sch_references_equi, sch_historique,
unnest((string_to_array(sch_historique, 'strain'))[2:]) AS strain
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique != ''
AND sch_historique LIKE '%strain%'
AND sch_references_equi NOT LIKE '%strain%') AS a

ORDER BY xxx_id;
