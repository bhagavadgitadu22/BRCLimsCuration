SELECT ARRAY_AGG(xxx_id), ARRAY_AGG(sch_par_milieu_json), ref_equi FROM

(SELECT xxx_id, sch_par_milieu_json, REGEXP_MATCHES(mil_commentaire_compo, '[a-zA-Z]+ [0-9]+', 'g') AS ref_equi
FROM 
 
(SELECT t_milieu.xxx_id, mil_designation_en, mil_clg_id, mil_commentaire_compo,
jsonb_build_object(mil_designation_en, ARRAY_AGG(sch_identifiant)) AS sch_par_milieu_json
FROM 
t_milieu
LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id

GROUP BY t_milieu.xxx_id, mil_designation_en, mil_clg_id, mil_commentaire_compo) AS schs_par_milieu

WHERE mil_clg_id = 401
AND mil_commentaire_compo != ''
ORDER BY xxx_id) AS a

GROUP BY ref_equi
HAVING COUNT(*) > 1
ORDER BY ARRAY_AGG(sch_par_milieu_json);
