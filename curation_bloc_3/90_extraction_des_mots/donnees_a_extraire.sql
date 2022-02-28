DROP TABLE IF EXISTS ids_mots;

SELECT xxx_id 
INTO ids_mots
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_mot IS True;

SELECT * 
FROM t_souche
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Basonyme') AS t_basonyme
ON t_basonyme.att_col_id = t_souche.sch_col_id
AND t_basonyme.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Code produit collection') AS t_cpc
ON t_cpc.att_col_id = t_souche.sch_col_id
AND t_cpc.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Date de validation') AS t_date_validation
ON t_date_validation.att_col_id = t_souche.sch_col_id
AND t_date_validation.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Valeur 1') AS t_valeur1
ON t_valeur1.att_col_id = t_souche.sch_col_id
AND t_valeur1.svl_entite_id = t_souche.xxx_id
WHERE xxx_id IN (SELECT xxx_id FROM ids_mots);

SELECT * 
FROM t_lot
JOIN t_souche
ON lot_sch_id = t_souche.xxx_id
WHERE sch_mot IS True;
--AND t_lot.xxx_sup_dat IS NULL;

SELECT * 
FROM t_souche
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Basonyme') AS t_basonyme
ON t_basonyme.att_col_id = t_souche.sch_col_id
AND t_basonyme.svl_entite_id = t_souche.xxx_id
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_mot IS True;

SELECT sch_identifiant, sch_version, att_nom, svl_valeur 
FROM t_attribut 
LEFT JOIN t_string_val 
ON t_string_val.svl_att_id = t_attribut.xxx_id
JOIN t_souche
ON att_col_id = t_souche.sch_col_id
AND svl_entite_id = t_souche.xxx_id
WHERE sch_mot IS True
AND svl_valeur NOT SIMILAR TO '[ ]*'
ORDER BY sch_identifiant, sch_version;

SELECT DISTINCT att_nom
FROM t_attribut 
LEFT JOIN t_string_val 
ON t_string_val.svl_att_id = t_attribut.xxx_id
JOIN t_souche
ON att_col_id = t_souche.sch_col_id
AND svl_entite_id = t_souche.xxx_id
WHERE sch_mot IS True
AND svl_valeur NOT SIMILAR TO '[ ]*';



