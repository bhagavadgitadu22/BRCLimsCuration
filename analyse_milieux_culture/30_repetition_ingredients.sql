SELECT ARRAY_AGG(xxx_id), ARRAY_AGG(mil_designation_en), arr FROM 

(SELECT t_milieu.xxx_id, mil_designation_en,
ARRAY_AGG(cmp_designation_en ORDER BY cmp_designation_en) AS arr
FROM t_milieu
JOIN t_milieu_composition
ON lmc_mil_id = t_milieu.xxx_id
JOIN t_composition
ON lmc_cmp_id = t_composition.xxx_id
WHERE mil_clg_id = 401
GROUP BY t_milieu.xxx_id, mil_designation_en) AS a

GROUP BY arr
HAVING COUNT(*) > 1
ORDER BY ARRAY_AGG(mil_designation_en);
