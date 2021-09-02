SELECT ARRAY_AGG(xxx_id), ARRAY_AGG(sch_par_milieu_json), recette, COUNT(*) FROM

(SELECT xxx_id, ARRAY_AGG(full_ingredient ORDER BY full_ingredient) AS recette,
sch_par_milieu_json FROM
 
(SELECT a.xxx_id, CONCAT(a.ingredient, ' : ', a.quantite, ' ', a.unite) AS full_ingredient,
sch_par_milieu_json FROM
 
(SELECT schs_par_milieu.xxx_id,
lmc_qte AS quantite,
t_donneedico.don_lib AS unite,
cmp_designation_en AS ingredient,
sch_par_milieu_json
FROM 
 
(SELECT t_milieu.xxx_id, mil_designation_en, mil_clg_id, 
jsonb_build_object(mil_designation_en, ARRAY_AGG(sch_identifiant)) AS sch_par_milieu_json
FROM 
t_milieu
LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id

GROUP BY t_milieu.xxx_id, mil_designation_en, mil_clg_id) AS schs_par_milieu 

JOIN t_milieu_composition
ON lmc_mil_id = schs_par_milieu.xxx_id
JOIN t_composition
ON lmc_cmp_id = t_composition.xxx_id
JOIN t_donneedico
ON t_donneedico.xxx_id = lmc_unite
WHERE mil_clg_id = 401) AS a) AS b

GROUP BY xxx_id, sch_par_milieu_json) AS c
GROUP BY recette
HAVING COUNT(*) > 1
ORDER BY ARRAY_AGG(sch_par_milieu_json);
