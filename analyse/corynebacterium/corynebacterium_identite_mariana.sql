SELECT * FROM
(SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_id,

sch_denomination AS denomination, col_nom AS collection, sch_synonymes AS synonymes, 
sch_identifiant AS identifiant, sch_dat_acquisition AS date_acquisition, t_depot.don_lib AS deposant,
sch_type, sch_com_identite AS commentaires, sch_autres_coll,
sch_proprietes, sch_references_equi, sch_historique,
t_reception.dvl_valeur AS date_de_reception,
t_validation.svl_valeur AS date_de_validation, 
t_basonyme.svl_valeur AS basonyme, 

t_approbation.dvl_valeur AS date_d_approbation, 

t_lieu.don_lib AS lieu_origine, sch_lieu_precis AS lieu_precis_origine,
sch_dat_prelevement, sch_nature_prelevement, 
sch_dat_isolement, sch_isole_a_partir_de, 
 
CASE WHEN t_antibiogramme.xxx_id IS NULL THEN 'N'
	ELSE 'Y'
END AS antibiogrammes, ant_dat_realisation, ant_com, 

sch_bibliographie

FROM t_souche
LEFT JOIN t_collection
ON sch_col_id = t_collection.xxx_id

LEFT JOIN (SELECT * FROM t_date_val AS t_date_reception
JOIN t_attribut AS t_att_reception
ON t_date_reception.dvl_att_id = t_att_reception.xxx_id
AND t_att_reception.att_nom = 'Date de réception') AS t_reception
ON t_reception.dvl_entite_id = t_souche.xxx_id

LEFT JOIN (SELECT * FROM t_string_val AS t_date_validation
JOIN t_attribut AS t_att_validation
ON t_date_validation.svl_att_id = t_att_validation.xxx_id
AND t_att_validation.att_nom = 'Date de validation') AS t_validation
ON t_validation.svl_entite_id = t_souche.xxx_id

LEFT JOIN (SELECT * FROM t_string_val AS t_basonyme
JOIN t_attribut AS t_att_basonyme
ON t_basonyme.svl_att_id = t_att_basonyme.xxx_id
AND t_att_basonyme.att_nom = 'Basonyme') AS t_basonyme
ON t_basonyme.svl_entite_id = t_souche.xxx_id

LEFT JOIN (SELECT * FROM t_date_val AS t_date_approbation
JOIN t_attribut AS t_att_approbation
ON t_date_approbation.dvl_att_id = t_att_approbation.xxx_id
AND t_att_approbation.att_nom = 'Date d''approbation') AS t_approbation
ON t_approbation.dvl_entite_id = t_souche.xxx_id
 
LEFT JOIN t_donneedico AS t_depot
ON t_depot.xxx_id = sch_depositaire
 
LEFT JOIN t_donneedico AS t_lieu
ON t_lieu.xxx_id = sch_lieu
 
LEFT JOIN t_antibiogramme
ON t_souche.xxx_id = ant_sch_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM t_souche)
AND sch_denomination LIKE 'Corynebacterium%'

ORDER BY sch_identifiant, sch_version DESC) AS a
ORDER BY xxx_id;
