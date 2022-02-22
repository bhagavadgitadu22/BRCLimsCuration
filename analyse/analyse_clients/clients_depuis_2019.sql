SELECT clt_code, clt_fact_raison_sociale, ARRAY_AGG(DISTINCT cor_email) FILTER (WHERE cor_email != ''),
array_length(ARRAY_AGG(EXTRACT(YEAR FROM cmd_dat)), 1) AS nombre,
MAX(EXTRACT(YEAR FROM cmd_dat)) AS last_visit
FROM t_client
LEFT JOIN t_correspondant
ON cor_clt_id = t_client.xxx_id
JOIN t_commande
ON cmd_clt_id = t_client.xxx_id
WHERE EXTRACT(YEAR FROM cmd_dat) >= 2019
GROUP BY clt_code, clt_fact_raison_sociale
ORDER BY array_length(ARRAY_AGG(EXTRACT(YEAR FROM cmd_dat)), 1) DESC
