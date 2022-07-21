SELECT COUNT(*),
(string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[1] AS genus,
(string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[2] AS species,
CASE
	WHEN (string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[3]
	ELSE ''
END AS subspecies
FROM t_souche
LEFT JOIN t_collection
ON t_collection.xxx_id = sch_col_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY (string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[1], (string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[2], CASE
	WHEN (string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(REPLACE(sch_denomination, '"', ''), ' '))[3]
	ELSE '' END;
