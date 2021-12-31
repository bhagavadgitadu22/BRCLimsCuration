SELECT sch.sch_identifiant, type_sch.sch_identifiant
FROM t_souche AS sch
JOIN t_souche AS type_sch
ON type_sch.sch_identifiant = CONCAT(sch.sch_identifiant, 'T')
WHERE sch.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);
