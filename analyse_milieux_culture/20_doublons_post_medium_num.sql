SELECT ARRAY_AGG(xxx_id), ARRAY_AGG(sch_par_milieu_json), arr FROM

(SELECT xxx_id, 
(REGEXP_MATCHES(mil_designation_en, 'MEDIUM [0-9]+ - (.*)'))[1] as arr,
sch_par_milieu_json

FROM 
 
(SELECT t_milieu.xxx_id, mil_designation_en, mil_clg_id, 
jsonb_build_object(mil_designation_en, ARRAY_AGG(sch_identifiant)) AS sch_par_milieu_json
FROM 
t_milieu
LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id

GROUP BY t_milieu.xxx_id, mil_designation_en, mil_clg_id) AS schs_par_milieu
 
WHERE mil_clg_id = 401
AND mil_designation_en SIMILAR TO '%MEDIUM [0-9]+ -%') AS a

GROUP BY arr
HAVING COUNT(*) > 1
ORDER BY ARRAY_AGG(sch_par_milieu_json);
