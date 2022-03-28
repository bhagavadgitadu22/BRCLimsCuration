SELECT cmd_dat, cmd_code, clt_code, cmd_envoi_gratuit
FROM t_commande
LEFT JOIN t_client
ON cmd_clt_id = t_client.xxx_id
WHERE EXTRACT(YEAR FROM cmd_dat) = 2021
AND t_commande.xxx_sup_dat IS NULL
ORDER BY cmd_dat;

SELECT xxx_cre_dat, clt_code
FROM t_client
WHERE EXTRACT(YEAR FROM xxx_cre_dat) = 2021
ORDER BY xxx_cre_dat;
