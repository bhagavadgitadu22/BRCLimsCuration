UPDATE t_souche
SET sch_temperature_incubation = REPLACE(sch_temperature_incubation, '°C', '')
WHERE sch_temperature_incubation LIKE '%°C%';

UPDATE t_souche
SET sch_temperature_incubation = REPLACE(sch_temperature_incubation, '°', '')
WHERE sch_temperature_incubation LIKE '%°%';

UPDATE t_souche
SET sch_temperature_incubation = TRIM(sch_temperature_incubation)
WHERE sch_temperature_incubation != TRIM(sch_temperature_incubation);

UPDATE t_souche
SET sch_temperature_incubation = '37'
WHERE sch_temperature_incubation = '37 aérobie';

SELECT sch_identifiant, sch_temperature_incubation, COUNT(*)
FROM t_souche
WHERE sch_temperature_incubation NOT SIMILAR TO '[0-9]*'
GROUP BY sch_identifiant, sch_temperature_incubation
ORDER BY COUNT(*) DESC;