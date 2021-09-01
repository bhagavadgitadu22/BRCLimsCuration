SELECT xxx_id, mil_designation_en
FROM t_milieu
WHERE mil_clg_id = 401
AND mil_designation_en NOT SIMILAR TO '%MEDIUM [0-9]+ -%'
GROUP BY xxx_id, mil_designation_en;
