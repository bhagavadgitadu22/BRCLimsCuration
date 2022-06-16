SELECT sch_identifiant, path, sch_denomination, sch_references_equi, 
cpr_com, sch_type, sch_catalogue, sch_historique, t_lieu.don_lib, 
sch_isole_a_partir_de, EXTRACT(YEAR FROM sch_dat_acquisition)
FROM t_souche

LEFT JOIN chemins_taxonomie
ON chemins_taxonomie.sch_taxonomie = t_souche.sch_taxonomie
LEFT JOIN t_donneedico AS t_lieu
ON sch_lieu = t_lieu.xxx_id

LEFT JOIN (SELECT * FROM t_carac_phenotypique_resultat AS t_cpr_1546
JOIN t_carac_phenotypique AS t_cp_1546
ON t_cp_1546.xxx_id = t_cpr_1546.cpr_cpy_id
AND t_cp_1546.cpy_numero = 1546) AS a
ON t_souche.xxx_id = a.cpr_sch_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND t_lieu.don_lib = 'Antarctica';