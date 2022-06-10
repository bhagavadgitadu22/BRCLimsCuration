DROP TABLE IF EXISTS new_origines_cip;

SELECT last_version_souches_cip.xxx_id AS sch_id, t_donneedico.xxx_id AS dico_id, don_lib, origine, isole
INTO new_origines_cip
FROM dsm_origines
LEFT JOIN last_version_souches_cip
ON sch_identifiant = identifier
LEFT JOIN t_donneedico
ON don_lib = origine
AND don_dic_id = 102
AND t_donneedico.xxx_sup_dat IS NULL;

UPDATE t_souche
SET sch_origine = dico_id,
	sch_isole_a_partir_de = CONCAT(UPPER(LEFT(isole, 1)), RIGHT(isole, -1))
FROM new_origines_cip
WHERE t_souche.xxx_id = sch_id;
