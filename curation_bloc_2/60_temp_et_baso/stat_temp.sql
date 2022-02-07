/*
SELECT sch_temps_culture, ascii(LEFT(sch_temps_culture, 1)),
sch_temperature_incubation, ARRAY_AGG(sch_identifiant)
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND xxx_sup_dat IS NULL
AND (sch_temperature_incubation NOT SIMILAR TO '[0-9]+'
OR sch_temps_culture NOT SIMILAR TO '%[a-zA-Z0-9]+%')
GROUP BY sch_temps_culture, sch_temperature_incubation;
*/

SELECT sch_temps_culture, COUNT(*), ARRAY_AGG(sch_identifiant)
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture NOT SIMILAR TO '[0-9]+(-[0-9]+)* (H|D|W|M)'
GROUP BY sch_temps_culture;
