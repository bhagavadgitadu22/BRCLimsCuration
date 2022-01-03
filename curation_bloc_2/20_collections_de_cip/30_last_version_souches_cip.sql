DROP TABLE IF EXISTS last_version_souches_cip;

SELECT DISTINCT ON (sch_identifiant) 
xxx_id, sch_identifiant, sch_version, 
trim(sch_denomination) AS sch_denomination,
REGEXP_MATCHES(sch_denomination, '.*?(?=[A-Z]+[^a-zA-Z]+|[A-Z]{1}?[0-9]+)'), 
(REGEXP_MATCHES(sch_denomination, '[A-Z]{1}[a-z]+ [a-z]+( [a-z]+)?'))[1]
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND xxx_sup_dat IS NULL
ORDER BY sch_identifiant, sch_version DESC;
