SELECT EXTRACT(YEAR FROM t_client.xxx_cre_dat), COUNT(*) 
FROM t_client 
LEFT JOIN t_commande
ON cmd_clt_id = t_client.xxx_id
WHERE t_commande.xxx_id IS NULL
GROUP BY EXTRACT(YEAR FROM t_client.xxx_cre_dat)
ORDER BY EXTRACT(YEAR FROM t_client.xxx_cre_dat);
