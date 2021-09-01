SELECT arr FROM 
(SELECT t_milieu.xxx_id,
array_agg(cmp_designation_en ORDER BY cmp_designation_en) AS arr
FROM t_milieu
JOIN t_milieu_composition
ON lmc_mil_id = t_milieu.xxx_id
JOIN t_composition
ON lmc_cmp_id = t_composition.xxx_id
WHERE mil_designation_en SIMILAR TO '%MEDIUM [0-9]+ -%'
GROUP BY t_milieu.xxx_id) AS a
GROUP BY arr
HAVING COUNT(*) > 1;
