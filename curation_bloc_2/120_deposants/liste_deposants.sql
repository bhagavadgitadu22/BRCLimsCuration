SELECT t_categorie.don_lib, t_deposant.don_lib, COUNT(*), ARRAY_AGG(sch_identifiant)
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
--WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
GROUP BY t_categorie.don_lib, t_deposant.don_lib
ORDER BY t_categorie.don_lib, t_deposant.don_lib;
