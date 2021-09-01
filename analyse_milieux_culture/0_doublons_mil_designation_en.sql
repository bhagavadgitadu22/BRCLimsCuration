SELECT ARRAY_AGG(xxx_id), mil_designation_en
FROM t_milieu
WHERE mil_clg_id = 401
GROUP BY mil_designation_en
HAVING COUNT(*) > 1;
