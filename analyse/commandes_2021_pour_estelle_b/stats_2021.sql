SELECT cmd_num_bon_livraison, cmd_dat, clt_fact_raison_sociale, code_tarif, array_to_string(ARRAY_AGG(qte), ', ') FROM
(SELECT cmd_num_bon_livraison, cmd_dat, clt_fact_raison_sociale, don_lib AS code_tarif, CONCAT(sch_identifiant, ': ', COUNT(*)) AS qte
FROM t_commande
LEFT JOIN t_client
ON cmd_clt_id = t_client.xxx_id
LEFT JOIN t_donneedico
ON clt_code_tarif = t_donneedico.xxx_id
LEFT JOIN t_article_commande
ON t_commande.xxx_id = acm_cmd_id
LEFT JOIN t_lot
ON acm_lot_id = t_lot.xxx_id
LEFT JOIN t_souche 
ON lot_sch_id = t_souche.xxx_id
WHERE EXTRACT(YEAR FROM cmd_dat) = 2021
AND cmd_envoi_gratuit IS True
GROUP BY cmd_num_bon_livraison, cmd_dat, clt_fact_raison_sociale, code_tarif, sch_identifiant) AS a
GROUP BY cmd_num_bon_livraison, cmd_dat, clt_fact_raison_sociale, code_tarif;
