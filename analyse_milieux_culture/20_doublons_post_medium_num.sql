SELECT array_agg(xxx_id), arr FROM
(SELECT xxx_id, (REGEXP_MATCHES(mil_designation_en, 'MEDIUM [0-9]+ - (.*)'))[1] as arr
FROM t_milieu
WHERE mil_clg_id = 401
AND mil_designation_en SIMILAR TO '%MEDIUM [0-9]+ -%') AS a
GROUP BY arr
HAVING COUNT(*) > 1;
