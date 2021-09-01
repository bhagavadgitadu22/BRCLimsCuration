SELECT mil_designation_en, (REGEXP_MATCHES(mil_designation_en, 'MEDIUM [0-9]+ - (.*)'))[1]
FROM t_milieu
WHERE mil_designation_en SIMILAR TO '%MEDIUM [0-9]+ -%'
GROUP BY mil_designation_en
