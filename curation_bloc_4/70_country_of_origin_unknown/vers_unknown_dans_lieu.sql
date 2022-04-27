DROP TABLE IF EXISTS lieu_unknown;

SELECT t_collection.xxx_id AS col_id, col_nom, t_donneedico.xxx_id AS dic_id, don_lib
INTO lieu_unknown
FROM t_donneedico 
JOIN t_dico ON don_dic_id = t_dico.xxx_id 
JOIN t_collection ON CONCAT('[', col_clg_id, ']') = dic_grp_collection
WHERE dic_nom = 'Localisation'
AND t_collection.xxx_id = 413
AND t_donneedico.xxx_sup_dat IS NOT NULL
AND don_lib = 'Unknown';

SELECT sch_lieu_precis FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_lieu_precis LIKE '%Country of origin unknown%';

UPDATE t_souche
SET sch_lieu = (SELECT dic_id FROM lieu_unknown),
	sch_lieu_precis = ''
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_lieu_precis LIKE '%Country of origin unknown%';
