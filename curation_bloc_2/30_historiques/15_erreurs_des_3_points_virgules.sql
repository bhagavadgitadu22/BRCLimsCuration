UPDATE t_souche
SET sch_historique = regexp_replace(sch_historique, ';;;.*', '')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%;;;%';
