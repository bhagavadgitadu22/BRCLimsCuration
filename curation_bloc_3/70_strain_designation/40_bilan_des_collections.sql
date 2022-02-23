DROP TABLE IF EXISTS bilan_collections;

SELECT t_deposant.don_lib AS collection
INTO bilan_collections
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
WHERE t_categorie.don_lib = 'Collections'
GROUP BY t_deposant.don_lib
ORDER BY t_deposant.don_lib;
