SELECT COUNT(*) FROM
(SELECT * 
FROM t_souche
WHERE sch_taxonomie IS NOT NULL) AS a;
