SELECT clt_code, clt_fact_raison_sociale, mails,
array_length(ARRAY_AGG(EXTRACT(YEAR FROM cmd_dat)), 1) AS nombre,
MAX(EXTRACT(YEAR FROM cmd_dat)) AS last_visit
FROM t_client
LEFT JOIN (SELECT cor_clt_id, ARRAY_AGG(DISTINCT cor_email) FILTER (WHERE cor_email != '') AS mails FROM t_correspondant GROUP BY cor_clt_id) AS t_mails
ON t_mails.cor_clt_id = t_client.xxx_id
JOIN t_commande
ON cmd_clt_id = t_client.xxx_id
WHERE EXTRACT(YEAR FROM cmd_dat) >= 2019
GROUP BY clt_code, clt_fact_raison_sociale, mails
ORDER BY array_length(ARRAY_AGG(EXTRACT(YEAR FROM cmd_dat)), 1) DESC
