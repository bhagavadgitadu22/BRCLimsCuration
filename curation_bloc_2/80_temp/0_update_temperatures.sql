SELECT sch.sch_identifiant, type_sch.sch_identifiant, sch.sch_temperature_incubation, type_sch.sch_temperature_incubation
FROM t_souche AS sch
JOIN t_souche AS type_sch
ON type_sch.sch_identifiant = CONCAT(sch.sch_identifiant, 'T')
WHERE sch.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND type_sch.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch.sch_temperature_incubation NOT SIMILAR TO '[0-9]+';
