SELECT EXTRACT(YEAR FROM cmd_dat), sum(acm_quantite)::integer
FROM t_commande
JOIN t_client
ON cmd_clt_id = t_client.xxx_id
JOIN t_donneedico
ON clt_fact_pays = t_donneedico.xxx_id
JOIN t_article_commande
ON t_commande.xxx_id = acm_cmd_id
WHERE don_lib = 'FRANCE'
GROUP BY EXTRACT(YEAR FROM cmd_dat)
ORDER BY EXTRACT(YEAR FROM cmd_dat);
