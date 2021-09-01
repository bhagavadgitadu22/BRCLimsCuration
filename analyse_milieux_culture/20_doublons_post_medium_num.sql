SELECT (REGEXP_MATCHES(mil_designation_en, 'MEDIUM [0-9]+ - (.*)'))[1]
FROM t_milieu
WHERE mil_designation_en SIMILAR TO '%MEDIUM [0-9]+ -%'
GROUP BY (REGEXP_MATCHES(mil_designation_en, 'MEDIUM [0-9]+ - (.*)'))[1]
HAVING COUNT(*) > 1
