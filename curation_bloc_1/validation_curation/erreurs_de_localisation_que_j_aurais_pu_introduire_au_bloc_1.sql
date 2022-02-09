SELECT t_souche.xxx_id, sch_identifiant, sch_lieu_precis, don_lib FROM t_souche 
JOIN t_donneedico 
ON sch_lieu = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND (LOWER(don_lib) LIKE '%congo%'
	OR sch_lieu_precis LIKE '%congo%');
