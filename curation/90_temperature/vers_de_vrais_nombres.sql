UPDATE t_souche
SET sch_temperature_incubation = REPLACE(sch_temperature_incubation, CONCAT(CHR(176), 'C'), '')
WHERE sch_temperature_incubation LIKE CONCAT('%', CHR(176), 'C%')
AND xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_temperature_incubation = REPLACE(sch_temperature_incubation, CHR(176), '')
WHERE sch_temperature_incubation LIKE CONCAT('%', CHR(176), '%')
AND xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_temperature_incubation = TRIM(sch_temperature_incubation)
WHERE sch_temperature_incubation != TRIM(sch_temperature_incubation)
AND xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_temperature_incubation = '37'
WHERE sch_temperature_incubation = '37 aérobie'
AND xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

/*
SELECT sch_identifiant, sch_temperature_incubation, COUNT(*)
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temperature_incubation NOT SIMILAR TO '[0-9]*'
GROUP BY sch_identifiant, sch_temperature_incubation
ORDER BY COUNT(*) DESC;
*/
