SELECT EXTRACT(YEAR FROM cmd_dat), clt_fact_raison_sociale, acad_ou_indus(don_lib::integer, clt_fact_raison_sociale), COUNT(*)
FROM t_commande
JOIN t_client
ON cmd_clt_id = t_client.xxx_id
JOIN t_donneedico
ON t_donneedico.xxx_id = clt_code_tarif
JOIN t_article_commande
ON t_commande.xxx_id = acm_cmd_id
GROUP BY EXTRACT(YEAR FROM cmd_dat), clt_fact_raison_sociale, acad_ou_indus(don_lib::integer, clt_fact_raison_sociale)
ORDER BY EXTRACT(YEAR FROM cmd_dat), acad_ou_indus(don_lib::integer, clt_fact_raison_sociale), -COUNT(*);
