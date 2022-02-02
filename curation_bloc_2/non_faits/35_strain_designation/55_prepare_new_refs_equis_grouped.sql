DROP TABLE IF EXISTS new_refs_equis_grouped;

SELECT xxx_id, short_strain, MIN(number_row) AS position
INTO TABLE new_refs_equis_grouped
FROM new_refs_equis
GROUP BY xxx_id, short_strain;

DELETE FROM new_refs_equis_grouped
WHERE LOWER(short_strain) LIKE '%cpc%';

DELETE FROM new_refs_equis_grouped
WHERE LOWER(short_strain) LIKE '%::%'
OR LOWER(short_strain) LIKE CONCAT('%', CHR(916), '%');

DELETE FROM new_refs_equis_grouped AS a
USING new_refs_equis_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND a.short_strain = ANY(string_to_array(REGEXP_REPLACE(b.short_strain, '[- \/]+', ' ', 'g'), ' '));

DELETE FROM new_refs_equis_grouped AS a
USING new_refs_equis_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND REPLACE(b.short_strain, ' ', '') LIKE CONCAT('%', REPLACE(a.short_strain, ' ', ''), '%')
AND length(a.short_strain) > 3;
