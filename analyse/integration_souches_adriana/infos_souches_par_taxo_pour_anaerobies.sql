SELECT CONCAT((string_to_array(sch_denomination, ' '))[1], ' ', (string_to_array(sch_denomination, ' '))[2], ' ', CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END) AS taxon_name, COUNT(*), ARRAY_AGG(sch_identifiant)
FROM 

(SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, 
sch_references_equi, sch_historique, sch_dat_isolement, 
sch_isole_a_partir_de, sch_catalogue, tai.don_lib AS atm_incub,
CASE 
      WHEN t_lot_short.lot_sch_id IS NULL THEN 'false'
      ELSE 'true'
END AS presence_lot
FROM t_souche
LEFT JOIN (SELECT DISTINCT lot_sch_id FROM t_lot WHERE xxx_sup_dat IS NULL AND lot_qte_stock != 0) AS t_lot_short
ON t_souche.xxx_id = t_lot_short.lot_sch_id
LEFT JOIN t_donneedico AS tai
ON tai.xxx_id = sch_atmosphere_incubation 
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
ORDER BY t_souche.xxx_id) AS a

WHERE sch_catalogue IS True
/*WHERE sch_catalogue IS False
AND presence_lot = 'true'
AND LOWER(sch_denomination) NOT LIKE '%pas de souche%'
AND LOWER(sch_denomination) NOT LIKE '%doublon%'
AND LOWER(sch_denomination) NOT LIKE '%distribuer%'*/
AND LOWER(atm_incub) LIKE '%anaerobic%'
GROUP BY CONCAT((string_to_array(sch_denomination, ' '))[1], ' ', (string_to_array(sch_denomination, ' '))[2], ' ', CASE
	WHEN (string_to_array(sch_denomination, ' '))[3] SIMILAR TO '[a-z]+' THEN (string_to_array(sch_denomination, ' '))[3]
	ELSE ''
END)
ORDER BY COUNT(*) DESC;
