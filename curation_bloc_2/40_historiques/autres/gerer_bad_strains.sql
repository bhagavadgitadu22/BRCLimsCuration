/*
DROP TABLE IF EXISTS jointure;

SELECT DISTINCT short_strain, CONCAT(genus_name, ' ', sp_epithet) AS taxo
INTO TEMPORARY TABLE jointure
FROM bad_strains
JOIN taxonomy
ON short_strain LIKE CONCAT('%', genus_name, ' ', sp_epithet, '%');

SELECT short_strain, taxo, 
(string_to_array(short_strain, taxo))[1],
btrim((regexp_split_to_array((string_to_array(short_strain, taxo))[1], '(, |Flavobacterium|Sphingomonas)'))[1], ' ,.;')
FROM jointure
WHERE taxo SIMILAR TO '%[a-zA-Z]+ [a-zA-Z]+%'
AND (string_to_array(short_strain, taxo))[2] = ''
ORDER BY short_strain, taxo;
*/

DROP TABLE IF EXISTS jointure;

SELECT DISTINCT short_strain, genus_name AS taxo
INTO TEMPORARY TABLE jointure
FROM bad_strains
JOIN (SELECT DISTINCT genus_name FROM taxonomy) AS a
ON short_strain SIMILAR TO CONCAT('%', genus_name, ' [a-zA-Z]+[^0-9]*');

SELECT short_strain, taxo, 
(string_to_array(short_strain, taxo))[1]
FROM jointure
ORDER BY short_strain, taxo;

