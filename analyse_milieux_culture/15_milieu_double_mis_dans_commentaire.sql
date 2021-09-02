SELECT t_milieu.xxx_id, mil_designation_en, mil_commentaire_compo, array_remove(ARRAY_AGG(sch_identifiant), NULL)
FROM t_milieu
LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id
WHERE mil_clg_id = 401
AND LOWER(mil_commentaire_compo) LIKE '%medium%'
GROUP BY t_milieu.xxx_id, mil_designation_en, mil_clg_id;
