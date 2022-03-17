--code cpc à virer
DELETE FROM all_strains_grouped
WHERE LOWER(short_strain) LIKE '%cpc%';

--rien a faire la
DELETE FROM all_strains_grouped
WHERE LOWER(short_strain) LIKE '%::%'
OR LOWER(short_strain) LIKE CONCAT('%', CHR(916), '%');

-- virer les duplicats
DELETE FROM all_strains_grouped AS a
USING all_strains_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND a.short_strain = ANY(string_to_array(REGEXP_REPLACE(b.short_strain, '[- \/]+', ' ', 'g'), ' '));

--idem
DELETE FROM all_strains_grouped AS a
USING all_strains_grouped AS b
WHERE a.xxx_id = b.xxx_id
AND a.position != b.position
AND REPLACE(b.short_strain, ' ', '') LIKE CONCAT('%', REPLACE(a.short_strain, ' ', ''), '%')
AND length(a.short_strain) > 3;

--virer réfs équis des souches 2xxxxx que j'ai supprimé dans le bloc 1
DELETE FROM all_strains_grouped
WHERE short_strain IN (SELECT identifiant FROM deuxxxxx_supprimes);
