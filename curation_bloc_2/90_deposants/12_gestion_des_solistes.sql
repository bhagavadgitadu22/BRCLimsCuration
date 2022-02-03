DROP TABLE IF EXISTS solistes_utilises;

SELECT t_deposant.xxx_id, t_deposant.don_lib, trim(t_deposant.don_lib) AS nom
INTO solistes_utilises
FROM t_donneedico AS t_deposant
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
WHERE t_categorie.don_lib = CONCAT('D', CHR(233), 'posants')
AND (CHAR_LENGTH(t_deposant.don_lib) - CHAR_LENGTH(REPLACE(t_deposant.don_lib, ',', ''))) = 0
ORDER BY don_lib;

UPDATE t_donneedico
SET don_lib = CONCAT(nom, ', ', nom)
FROM solistes_utilises
WHERE solistes_utilises.xxx_id = t_donneedico.xxx_id;

UPDATE t_donneedico
SET don_lib = REPLACE(t_donneedico.don_lib, 'Institut Pasteur', 'Pasteur Institute')
FROM solistes_utilises
WHERE t_donneedico.xxx_id = solistes_utilises.xxx_id
AND don_dic_id = 104
AND t_donneedico.don_lib != REPLACE(t_donneedico.don_lib, 'Institut Pasteur', 'Pasteur Institute');
