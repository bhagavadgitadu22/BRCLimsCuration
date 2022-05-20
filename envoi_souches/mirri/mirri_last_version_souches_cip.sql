DROP TABLE IF EXISTS last_version_souches_cip;

SELECT * 
INTO TABLE last_version_souches_cip
FROM (SELECT DISTINCT ON (sch_cpt_id)
t_souche.xxx_id, sch_identifiant, sch_version, 
sch_dat_acquisition, sch_dat_pheno, sch_qualite_dat_approbation,
sch_type, sch_catalogue, sch_col_id,
trim(sch_denomination) AS sch_denomination,
sch_temperature_incubation, sch_temps_culture,
svl_valeur AS basonyme, sch_synonymes,
sch_proprietes, sch_bibliographie,
t_lieu.don_lib AS lieu_origine, sch_isole_a_partir_de,
sch_dat_prelevement, sch_dat_isolement, 
sch_taxonomie, sch_references_equi, sch_historique, 
sch_autres_coll, sch_depositaire, sch_pto_id
FROM t_souche

LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Basonyme') AS t_basonyme
ON t_basonyme.att_col_id = t_souche.sch_col_id
AND t_basonyme.svl_entite_id = t_souche.xxx_id

LEFT JOIN t_donneedico AS t_lieu
ON t_lieu.xxx_id = sch_lieu

WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND t_souche.xxx_sup_dat IS NULL
ORDER BY sch_cpt_id, sch_version DESC) AS a
ORDER BY RANDOM()
LIMIT 200;
