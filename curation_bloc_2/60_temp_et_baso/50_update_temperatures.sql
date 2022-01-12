DROP TABLE IF EXISTS t_temp_incubation;

SELECT sch.sch_identifiant, type_sch.sch_identifiant,
sch.sch_temperature_incubation, type_sch.sch_temperature_incubation,
denom
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.sch_temperature_incubation != type_sch.sch_temperature_incubation
AND sch.sch_temperature_incubation != '';

SELECT sch.xxx_id AS id, type_sch.xxx_id AS type_id,
sch.sch_temperature_incubation AS old_temp, type_sch.sch_temperature_incubation AS new_temp
INTO t_temp_incubation
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.sch_temperature_incubation != type_sch.sch_temperature_incubation
AND sch.sch_temperature_incubation = '';

UPDATE t_souche
SET sch_temperature_incubation = new_temp
FROM t_temp_incubation
WHERE xxx_id = id;
