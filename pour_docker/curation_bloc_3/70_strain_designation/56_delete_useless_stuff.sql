DELETE FROM all_strains_grouped
WHERE LOWER(short_strain) LIKE '%cpc%';

DELETE FROM all_strains_grouped
WHERE LOWER(short_strain) LIKE '%::%'
OR LOWER(short_strain) LIKE CONCAT('%', CHR(916), '%');

DELETE FROM all_strains_grouped AS a
USING all_strains_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND a.short_strain = ANY(string_to_array(REGEXP_REPLACE(b.short_strain, '[- \/]+', ' ', 'g'), ' '));

DELETE FROM all_strains_grouped AS a
USING all_strains_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND REPLACE(b.short_strain, ' ', '') LIKE CONCAT('%', REPLACE(a.short_strain, ' ', ''), '%')
AND length(a.short_strain) > 3;

DELETE FROM all_strains_grouped
WHERE short_strain IN (SELECT identifiant FROM deuxxxxx_supprimes);
