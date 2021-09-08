SELECT arr_ids, mil_designation_en, array_remove(ARRAY_AGG(sch_identifiant), NULL) FROM

(SELECT ARRAY_AGG(xxx_id) AS arr_ids, mil_designation_en
FROM t_milieu
WHERE mil_clg_id = 401
GROUP BY mil_designation_en
HAVING COUNT(*) > 1) AS a

LEFT JOIN t_milieu_souche
ON msc_mil_id = ANY(arr_ids)
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id

GROUP BY arr_ids, mil_designation_en;
