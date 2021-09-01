SELECT mil_clg_id, array_agg(mil_designation_en), COUNT(*)
FROM t_milieu
GROUP BY mil_clg_id