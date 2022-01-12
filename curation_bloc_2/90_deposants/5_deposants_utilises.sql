DROP TABLE IF EXISTS tous_utilises;
DROP TABLE IF EXISTS deposants_utilises;

SELECT t_deposant.xxx_id, t_deposant.don_lib, 
split_part(t_deposant.don_lib, ',', 1) AS nom, split_part(t_deposant.don_lib, ',', 2) AS entreprise
INTO TABLE tous_utilises
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
--WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
ORDER BY t_deposant.xxx_id;

SELECT t_deposant.xxx_id, t_deposant.don_lib, 
split_part(t_deposant.don_lib, ',', 1) AS nom, split_part(t_deposant.don_lib, ',', 2) AS entreprise
INTO TABLE deposants_utilises
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
--WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
WHERE t_categorie.don_lib = 'Déposants'
AND (CHAR_LENGTH(t_deposant.don_lib) - CHAR_LENGTH(REPLACE(t_deposant.don_lib, ',', ''))) != 0
ORDER BY t_deposant.xxx_id;
