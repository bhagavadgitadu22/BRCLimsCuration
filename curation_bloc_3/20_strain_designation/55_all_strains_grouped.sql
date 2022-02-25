DROP TABLE IF EXISTS all_strains_grouped;

SELECT xxx_id, short_strain, MIN(number_row) AS position
INTO TABLE all_strains_grouped
FROM all_strains
GROUP BY xxx_id, short_strain;
