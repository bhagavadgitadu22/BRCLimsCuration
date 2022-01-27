DROP TABLE IF EXISTS stats_de_dates;

SELECT last_version_souches_cip.xxx_id, sch_identifiant, 
sch_dat_acquisition, t_reception.dvl_valeur AS date_reception, t_validation.svl_valeur AS date_validation, 
sch_dat_pheno, t_approbation.dvl_valeur AS date_approbation, 
sch_dat_prelevement, sch_dat_isolement, 
sch_qualite_dat_approbation
INTO stats_de_dates
FROM last_version_souches_cip

LEFT JOIN (SELECT att_col_id, dvl_entite_id, dvl_valeur FROM t_attribut 
		   LEFT JOIN t_date_val ON t_date_val.dvl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date d''approbation') AS t_approbation
ON t_approbation.att_col_id = last_version_souches_cip.sch_col_id
AND t_approbation.dvl_entite_id = last_version_souches_cip.xxx_id

LEFT JOIN (SELECT att_col_id, dvl_entite_id, dvl_valeur FROM t_attribut 
		   LEFT JOIN t_date_val ON t_date_val.dvl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de réception') AS t_reception
ON t_reception.att_col_id = last_version_souches_cip.sch_col_id
AND t_reception.dvl_entite_id = last_version_souches_cip.xxx_id

LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de validation') AS t_validation
ON t_validation.att_col_id = last_version_souches_cip.sch_col_id
AND t_validation.svl_entite_id = last_version_souches_cip.xxx_id

ORDER BY last_version_souches_cip.xxx_id DESC;
