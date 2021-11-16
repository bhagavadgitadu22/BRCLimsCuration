SELECT mil_numero, mil_designation_fr, mil_commentaire, 
COUNT(*) AS liste_souches

FROM (SELECT mil_numero, mil_designation_fr, mil_commentaire, 
sch_identifiant
FROM t_milieu

LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id

WHERE mil_clg_id = 401
	 AND t_milieu.xxx_sup_dat IS NULL) AS a

GROUP BY mil_numero, mil_designation_fr, mil_commentaire

ORDER BY mil_numero;
