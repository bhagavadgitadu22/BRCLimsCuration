SELECT sch.xxx_id, type_sch.xxx_id, sch.sch_identifiant, type_sch.sch_identifiant, sch.sch_temps_culture, type_sch.sch_temps_culture
FROM t_souche AS sch
JOIN t_souche AS type_sch
ON type_sch.sch_identifiant = CONCAT(sch.sch_identifiant, 'T')
WHERE sch.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND type_sch.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch.sch_temps_culture NOT SIMILAR TO '[0-9]+(-[0-9]+)* (H|D|W|M)';

-- attention aux version aussi, prendre toujours info de last version et n'update que dernière aussi (?) !

SELECT sch.sch_identifiant, type_sch.sch_identifiant, sch.sch_temps_culture, type_sch.sch_temps_culture
FROM t_souche AS sch
LEFT JOIN t_souche AS type_sch
ON type_sch.sch_identifiant = CONCAT(sch.sch_identifiant, 'T')
WHERE sch.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch.sch_temps_culture NOT SIMILAR TO '[0-9]+(-[0-9]+)* (H|D|W|M)';
