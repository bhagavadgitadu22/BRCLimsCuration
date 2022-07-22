SELECT don_lib, total, 
array_length(before_2014, 1), array_to_string(before_2014, ', '),
array_length(in_2014, 1), array_to_string(in_2014, ', '),
array_length(after_2014, 1), array_to_string(after_2014, ', '),
array_length(no_date, 1), array_to_string(no_date, ', ')
FROM (SELECT don_lib, COUNT(*) AS total,
array_remove(ARRAY_AGG(CASE WHEN EXTRACT(YEAR FROM sch_dat_isolement) < 2014 THEN sch_identifiant END), NULL) AS before_2014,
array_remove(ARRAY_AGG(CASE WHEN EXTRACT(YEAR FROM sch_dat_isolement) = 2014 THEN sch_identifiant END), NULL) AS in_2014,
array_remove(ARRAY_AGG(CASE WHEN EXTRACT(YEAR FROM sch_dat_isolement) > 2014 THEN sch_identifiant END), NULL) AS after_2014,
array_remove(ARRAY_AGG(CASE WHEN EXTRACT(YEAR FROM sch_dat_isolement) IS NULL THEN sch_identifiant END), NULL) AS no_date
FROM t_souche
JOIN t_donneedico
ON t_donneedico.xxx_id = sch_lieu
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
GROUP BY don_lib
ORDER BY don_lib) AS a;
