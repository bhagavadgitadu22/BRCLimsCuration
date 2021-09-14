SELECT xxx_id, sch_identifiant, sch_references_equi, sch_historique, array_agg(strain) FROM
(SELECT xxx_id, sch_identifiant, sch_references_equi, sch_historique, 
 trim((regexp_matches(sch_historique, 'strain.*?(?=<-|->|, |<|$)', 'g'))[1]) AS strain
FROM t_souche
ORDER BY xxx_id) AS a
GROUP BY xxx_id, sch_identifiant, sch_references_equi, sch_historique
HAVING COUNT(*) > 1