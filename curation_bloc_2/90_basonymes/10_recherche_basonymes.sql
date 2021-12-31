SELECT t_souche.xxx_id, sch_identifiant, sch_denomination, svl_valeur AS basonyme
FROM t_string_val 
JOIN t_souche
ON svl_entite_id = t_souche.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND svl_att_id = 2756
AND svl_valeur != '';
