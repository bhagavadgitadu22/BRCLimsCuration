SELECT ARRAY_AGG(xxx_id), ARRAY_AGG(mil_designation_en), recette, COUNT(*) FROM

(SELECT xxx_id, mil_designation_en, ARRAY_AGG(full_ingredient ORDER BY full_ingredient) AS recette FROM
 
(SELECT a.xxx_id, a.mil_designation_en, CONCAT(a.ingredient, ', ', a.quantite, ', ', a.unite) AS full_ingredient FROM
 
(SELECT t_milieu.xxx_id,
t_milieu.mil_designation_en,
lmc_qte AS quantite,
t_donneedico.don_lib AS unite,
cmp_designation_en AS ingredient
FROM t_milieu
JOIN t_milieu_composition
ON lmc_mil_id = t_milieu.xxx_id
JOIN t_composition
ON lmc_cmp_id = t_composition.xxx_id
JOIN t_donneedico
ON t_donneedico.xxx_id = lmc_unite
WHERE mil_clg_id = 401) AS a) AS b

GROUP BY xxx_id, mil_designation_en) AS c
GROUP BY recette
HAVING COUNT(*) > 1
