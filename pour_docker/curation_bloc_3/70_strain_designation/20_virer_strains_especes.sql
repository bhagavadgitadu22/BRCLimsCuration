DROP TABLE IF EXISTS bad_strains;
DROP TABLE IF EXISTS temp_taxo;

SELECT DISTINCT CONCAT('%', LOWER(genus_name), '%')
INTO TEMPORARY TABLE temp_taxo
FROM taxonomy
WHERE genus_name IS NOT NULL AND genus_name != '';

INSERT INTO temp_taxo
SELECT DISTINCT CONCAT('%', LOWER(sp_epithet), '%')
FROM taxonomy
WHERE CONCAT('%', LOWER(sp_epithet), '%') NOT IN (SELECT * FROM temp_taxo)
AND sp_epithet IS NOT NULL AND sp_epithet != '';

INSERT INTO temp_taxo
SELECT DISTINCT CONCAT('%', LOWER(subsp_epithet), '%')
FROM taxonomy
WHERE CONCAT('%', LOWER(subsp_epithet), '%') NOT IN (SELECT * FROM temp_taxo)
AND subsp_epithet IS NOT NULL AND subsp_epithet != '';

SELECT *
INTO bad_strains
FROM all_strains
WHERE LOWER(short_strain) LIKE ANY(array(SELECT * FROM temp_taxo));

DELETE 
FROM all_strains
WHERE LOWER(short_strain) LIKE ANY(array(SELECT * FROM temp_taxo));
