DROP TABLE IF EXISTS denoms_sans_taxos;
DROP TABLE IF EXISTS new_taxos;

SELECT *, CASE
	WHEN species = '' THEN genus
	WHEN subspecies = '' THEN CONCAT(genus, ' ', species)
	ELSE CONCAT(genus, ' ', species, ' ', subspecies)
END AS short_denom
INTO denoms_sans_taxos
FROM 
(SELECT t_souche.xxx_id, sch_identifiant, sch_denomination, 
(string_to_array(sch_denomination, ' '))[1] AS genus,
CASE
	WHEN (string_to_array(sch_denomination, ' '))[2] IS NULL THEN ''
	WHEN (string_to_array(sch_denomination, ' '))[2] SIMILAR TO 'sp.' THEN ''
	ELSE (string_to_array(sch_denomination, ' '))[2]
END AS species,
CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] IS NULL THEN ''
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END AS subspecies
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_taxonomie IS NULL
AND LOWER(sch_denomination) NOT SIMILAR TO '%(unnamed|pas de souche|corynéforme|unidentified|essai|doublon|inconnue|ommited)%'
AND sch_denomination SIMILAR TO '[A-Z]+%') AS a;

SELECT denoms_sans_taxos.xxx_id AS sch_id, 
chemins_taxonomie.sch_taxonomie AS path_id, 
short_denom, path
INTO new_taxos
FROM denoms_sans_taxos
JOIN chemins_taxonomie
ON short_denom = path;

UPDATE t_souche
SET sch_taxonomie = path_id
FROM new_taxos
WHERE t_souche.xxx_id = sch_id;
