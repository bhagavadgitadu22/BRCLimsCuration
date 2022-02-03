SELECT clt_code, MAX(EXTRACT(YEAR FROM t_commande.xxx_cre_dat)), MAX(EXTRACT(YEAR FROM t_commande.cmd_dat)), COUNT(*)
FROM t_client
JOIN t_correspondant
ON cor_clt_id = t_client.xxx_id
JOIN t_donneedico
ON clt_fact_pays = t_donneedico.xxx_id
LEFT JOIN t_commande
ON cmd_clt_id = t_client.xxx_id
WHERE t_commande.xxx_id IS NOT NULL 
AND clt_code NOT SIMILAR TO '10000%'
AND clt_code NOT SIMILAR TO 'tp%'
GROUP BY clt_code
ORDER BY MAX(EXTRACT(YEAR FROM t_commande.cmd_dat)) DESC, clt_code;
