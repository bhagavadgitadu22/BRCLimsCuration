SELECT clt_code, clt_fact_raison_sociale, 
COUNT(*) AS nombre_de_visites,
MAX(year) AS derniere_visite,
ROUND(((MAX(year)-MIN(year))/COUNT(*))::numeric,2) AS duree_moyenne_entre_2_visites,
MIN(temps_entre_visites),
MAX(temps_entre_visites),
ROUND(AVG(diversite_souches)::numeric,2) AS diversite_moyenne, ROUND(AVG(qte)::numeric,2) AS quantite_moyenne FROM

(SELECT clt_code, clt_fact_raison_sociale, EXTRACT(YEAR FROM cmd_dat) AS year, 
COUNT(*) AS diversite_souches, sum(acm_quantite)::integer AS qte,
 
LEAD(EXTRACT(YEAR FROM cmd_dat)) 
OVER (
    PARTITION BY clt_code, clt_fact_raison_sociale
    ORDER BY EXTRACT(YEAR FROM cmd_dat)
)-EXTRACT(YEAR FROM cmd_dat) AS temps_entre_visites

FROM t_client
JOIN t_commande
ON cmd_clt_id = t_client.xxx_id
JOIN t_article_commande
ON t_commande.xxx_id = acm_cmd_id
GROUP BY clt_code, clt_fact_raison_sociale, EXTRACT(YEAR FROM cmd_dat)
ORDER BY clt_code, clt_fact_raison_sociale, EXTRACT(YEAR FROM cmd_dat)) AS a

GROUP BY clt_code, clt_fact_raison_sociale
HAVING COUNT(*) > 1
ORDER BY derniere_visite DESC;
