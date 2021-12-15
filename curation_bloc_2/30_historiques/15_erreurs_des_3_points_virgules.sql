UPDATE t_souche
SET sch_historique = regexp_replace(sch_historique, ';;;.*', '')
WHERE sch_historique SIMILAR TO '%;;;%';
