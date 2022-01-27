DROP TABLE IF EXISTS all_strains_grouped;

SELECT xxx_id, short_strain, MIN(number_row) AS position
INTO TABLE all_strains_grouped
FROM all_strains
GROUP BY xxx_id, short_strain;

DELETE FROM all_strains_grouped AS a
USING all_strains_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND a.short_strain = ANY(string_to_array(REGEXP_REPLACE(b.short_strain, '[- \/]+', ' ', 'g'), ' '));

SELECT * 
FROM all_strains_grouped AS a
JOIN all_strains_grouped AS b
ON a.xxx_id = b.xxx_id
AND a.position != b.position
AND REPLACE(b.short_strain, ' ', '') LIKE CONCAT('%', a.short_strain, '%')
AND length(a.short_strain) > 3;

DELETE FROM all_strains_grouped AS a
USING all_strains_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND REPLACE(b.short_strain, ' ', '') LIKE CONCAT('%', a.short_strain, '%')
AND length(a.short_strain) > 3;
