SELECT * FROM
(SELECT sch_identifiant, sch_version, compte,
LAG(compte, 1) 
    OVER(
		PARTITION BY sch_identifiant
        ORDER BY sch_identifiant, sch_version
		RANGE BETWEEN 
            UNBOUNDED PRECEDING AND 
            UNBOUNDED FOLLOWING
    ) AS compte_precedent
FROM 
(SELECT sch_identifiant, sch_version, 
 CASE WHEN array_length(array_agg(t_lot.xxx_id) FILTER (WHERE t_lot.xxx_id IS NOT NULL), 1) IS NULL
		THEN 0
	  WHEN array_length(array_agg(t_lot.xxx_sup_dat) FILTER (WHERE t_lot.xxx_sup_dat IS NULL), 1) IS NOT NULL 
		THEN array_length(array_agg(t_lot.xxx_sup_dat) FILTER (WHERE t_lot.xxx_sup_dat IS NULL), 1) 
	  ELSE 0 END AS compte
FROM t_souche
LEFT JOIN t_lot
ON t_souche.xxx_id = t_lot.lot_sch_id
GROUP BY sch_identifiant, sch_version) AS a) AS b
WHERE compte_precedent != 0
ORDER BY sch_identifiant, sch_version;
