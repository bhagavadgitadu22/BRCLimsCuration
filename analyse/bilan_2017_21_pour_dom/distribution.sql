SELECT EXTRACT(YEAR FROM cmd_dat), sum(acm_quantite) as somme
FROM t_commande
JOIN t_client
ON cmd_clt_id = t_client.xxx_id
JOIN t_article_commande
ON t_commande.xxx_id = acm_cmd_id
JOIN t_lot
ON acm_lot_id = t_lot.xxx_id
JOIN t_souche
ON lot_sch_id = t_souche.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
GROUP BY EXTRACT(YEAR FROM cmd_dat)
ORDER BY EXTRACT(YEAR FROM cmd_dat) DESC;
