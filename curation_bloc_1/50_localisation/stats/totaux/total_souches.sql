SELECT COUNT(*) FROM
(SELECT * 
FROM t_souche
WHERE sch_lieu IS NOT NULL
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)) AS a;
