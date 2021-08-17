SELECT don_lib, unnest(ids) FROM
(SELECT don_lib, array_agg(t_souche.sch_identifiant) AS ids
FROM t_alerte_souche 
JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
JOIN t_souche ON als_sch_id = t_souche.xxx_id
WHERE don_dic_id IN (2698)
GROUP BY t_donneedico.xxx_id 
LIMIT 1 OFFSET 0) AS a;