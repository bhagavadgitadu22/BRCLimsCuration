DROP TABLE IF EXISTS t_temp_culture;

SELECT sch.sch_identifiant, type_sch.sch_identifiant,
sch.sch_temps_culture, type_sch.sch_temps_culture,
denom
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.sch_temps_culture != type_sch.sch_temps_culture
AND sch.sch_temps_culture != '';

SELECT sch.xxx_id AS id, type_sch.xxx_id AS type_id,
sch.sch_temps_culture AS old_temps, type_sch.sch_temps_culture AS new_temps
INTO t_temp_culture
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.sch_temps_culture != type_sch.sch_temps_culture
AND sch.sch_temps_culture = '';

UPDATE t_souche
SET sch_temps_culture = new_temps
FROM t_temp_culture
WHERE xxx_id = id;
