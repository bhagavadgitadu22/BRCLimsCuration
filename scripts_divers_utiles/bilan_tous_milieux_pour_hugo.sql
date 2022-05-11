SELECT mil_numero, mil_designation_fr, mil_commentaire, mil_commentaire_compo, 
ARRAY_AGG(DISTINCT partial_ingredient) AS partial_recette, ARRAY_AGG(DISTINCT full_ingredient) AS full_recette, 
array_length(ARRAY_AGG(DISTINCT sch_identifiant), 1), ARRAY_AGG(DISTINCT sch_identifiant) AS liste_souches

FROM (SELECT mil_numero, mil_designation_fr, mil_commentaire, mil_commentaire_compo, 
sch_identifiant,
CONCAT(cmp_designation_en, ' : ', lmc_qte, ' ', t_donneedico.don_lib, ' (', cmp_com, ')') AS full_ingredient, 
CONCAT(cmp_designation_en, ' : ', lmc_qte, ' ', t_donneedico.don_lib) AS partial_ingredient 
FROM t_milieu

LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN (SELECT * FROM t_souche WHERE xxx_sup_dat IS NULL) AS t_souche
ON t_souche.xxx_id = msc_sch_id

LEFT JOIN t_milieu_composition
ON lmc_mil_id = t_milieu.xxx_id
LEFT JOIN t_composition
ON lmc_cmp_id = t_composition.xxx_id
LEFT JOIN t_donneedico
ON t_donneedico.xxx_id = lmc_unite

WHERE mil_clg_id = 401
	 AND t_milieu.xxx_sup_dat IS NULL) AS a

GROUP BY mil_numero, mil_designation_fr, mil_commentaire, mil_commentaire_compo

ORDER BY mil_numero;
