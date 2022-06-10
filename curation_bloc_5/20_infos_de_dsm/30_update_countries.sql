DROP TABLE IF EXISTS new_countries_cip;

SELECT last_version_souches_cip.xxx_id AS sch_id, t_donneedico.xxx_id AS dico_id, don_lib, country, precision
INTO new_countries_cip
FROM dsm_countries
LEFT JOIN last_version_souches_cip
ON sch_identifiant = identifier
LEFT JOIN t_donneedico
ON don_lib = country
AND don_dic_id = 3758
AND t_donneedico.xxx_sup_dat IS NULL
WHERE country != '';

UPDATE t_souche
SET sch_lieu = dico_id,
	sch_lieu_precis = precision
FROM new_countries_cip
WHERE t_souche.xxx_id = sch_id;
