SELECT mil_designation_en
FROM t_milieu
GROUP BY mil_designation_en
HAVING COUNT(*) > 1

/*
(REGEXP_MATCHES(mil_designation_en, 'MEDIUM [0-9]+ - (.*)'))[1]
*/
