DROP TABLE IF EXISTS bad_strains;
DROP TABLE IF EXISTS temp_taxo;

SELECT DISTINCT CONCAT('%', genus_name, '%')
INTO TEMPORARY TABLE temp_taxo
FROM taxonomy
WHERE genus_name != '';

INSERT INTO temp_taxo
SELECT DISTINCT CONCAT('%', sp_epithet, '%')
FROM taxonomy
WHERE CONCAT('%', sp_epithet, '%') NOT IN (SELECT * FROM temp_taxo)
AND sp_epithet != '';

SELECT *
INTO bad_strains
FROM all_strains
WHERE short_strain LIKE ANY(array(SELECT * FROM temp_taxo));

DELETE 
FROM all_strains
WHERE short_strain LIKE ANY(array(SELECT * FROM temp_taxo));
