/*
SELECT t_donneedico.don_lib, CONCAT(nom, ', ', entreprise)
FROM t_donneedico
JOIN deposants_utilises
ON t_donneedico.xxx_id = deposants_utilises.xxx_id
WHERE don_dic_id = 104
AND t_donneedico.don_lib != CONCAT(nom, ', ', entreprise)
GROUP BY t_donneedico.don_lib, CONCAT(nom, ', ', entreprise);
*/

UPDATE t_donneedico
SET don_lib = CONCAT(nom, ', ', entreprise)
FROM deposants_utilises
WHERE t_donneedico.xxx_id = deposants_utilises.xxx_id
AND don_dic_id = 104
AND t_donneedico.don_lib != CONCAT(nom, ', ', entreprise);
