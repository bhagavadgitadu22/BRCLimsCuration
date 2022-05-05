DROP TABLE IF EXISTS list_of_taxos;
DROP TABLE IF EXISTS missing_taxos;
DROP TABLE IF EXISTS new_elmts_dicos;

SELECT genus AS name_taxo, 'genus'::text AS type_taxo
INTO list_of_taxos
FROM denoms_sans_taxos
GROUP BY genus;

INSERT INTO list_of_taxos
SELECT CONCAT(genus, ' ', species), 'species'
FROM denoms_sans_taxos
WHERE species != ''
GROUP BY CONCAT(genus, ' ', species);

INSERT INTO list_of_taxos
SELECT CONCAT(genus, ' ', species, ' ', subspecies), 'subspecies'
FROM denoms_sans_taxos
WHERE subspecies != ''
GROUP BY CONCAT(genus, ' ', species, ' ', subspecies);

-- on garde les dénoms sans taxos qui n'existent pas dans le dictionnaire des taxos
SELECT name_taxo, type_taxo
INTO missing_taxos
FROM list_of_taxos
LEFT JOIN chemins_taxonomie
ON name_taxo = path
WHERE path IS NULL
GROUP BY name_taxo, type_taxo;

UPDATE taxonomy
SET sp_epithet = ''
WHERE sp_epithet IS NULL;

UPDATE taxonomy
SET subsp_epithet = ''
WHERE subsp_epithet IS NULL;

-- croisement avec taxonomy pour voir ce qui existe dans lpsn
SELECT name_taxo, type_taxo, CASE
	WHEN sp_epithet = '' THEN genus_name
	WHEN subsp_epithet = '' THEN CONCAT(genus_name, ' ', sp_epithet)
	ELSE CONCAT(genus_name, ' ', sp_epithet, ' ', subsp_epithet)
END
INTO new_elmts_dicos
FROM missing_taxos
JOIN taxonomy
ON name_taxo = (CASE
	WHEN sp_epithet = '' THEN genus_name
	WHEN subsp_epithet = '' THEN CONCAT(genus_name, ' ', sp_epithet)
	ELSE CONCAT(genus_name, ' ', sp_epithet, ' ', subsp_epithet)
END)
GROUP BY name_taxo, type_taxo, CASE
	WHEN sp_epithet = '' THEN genus_name
	WHEN subsp_epithet = '' THEN CONCAT(genus_name, ' ', sp_epithet)
	ELSE CONCAT(genus_name, ' ', sp_epithet, ' ', subsp_epithet)
END
ORDER BY name_taxo;
