SELECT souches.xxx_id, souches.sch_identifiant, souches.sch_historique, 
country.don_lib AS dico_lieu, souches.sch_lieu_precis, souches.sch_dat_acquisition,
patho.don_lib AS dico_patho_animal, chemins_taxonomie.path AS dico_taxonomie, souches.sch_temperature_incubation
FROM 
(SELECT * FROM t_souche 
 JOIN (SELECT xxx_id AS sch_col_id, col_clg_id FROM t_collection) AS tc
 ON t_souche.sch_col_id = tc.sch_col_id
 WHERE tc.col_clg_id = 401) AS souches
LEFT JOIN t_donneedico AS country 
ON souches.sch_lieu = country.xxx_id
LEFT JOIN t_donneedico AS patho
ON souches.sch_patho_animal = patho.xxx_id
LEFT JOIN chemins_taxonomie
ON souches.sch_taxonomie = chemins_taxonomie.sch_taxonomie
WHERE (country.don_dic_id IS NULL 
	   OR country.don_dic_id IN (SELECT xxx_id FROM t_dico WHERE dic_grp_collection = '[401]' AND dic_nom = 'Localisation'))
AND (patho.don_dic_id IS NULL 
	 OR patho.don_dic_id IN (SELECT xxx_id FROM t_dico WHERE dic_grp_collection = '[401]' AND dic_nom = 'Pathogéncité Animal'))
AND (chemins_taxonomie.grp_collection IS NULL 
	 OR chemins_taxonomie.grp_collection = 401);
