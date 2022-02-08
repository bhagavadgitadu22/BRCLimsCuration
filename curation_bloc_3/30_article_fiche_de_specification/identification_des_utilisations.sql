SELECT sch_identifiant, lot_numero, don_lib 
FROM t_article_commande 
JOIN t_donneedico 
ON t_donneedico.xxx_id = acm_article 
JOIN t_lot
ON t_lot.xxx_id = acm_lot_id
JOIN t_souche
ON t_souche.xxx_id = lot_sch_id
WHERE LOWER(don_lib) LIKE '%spécification%'
AND t_lot.xxx_sup_dat IS NULL
AND t_souche.xxx_sup_dat IS NULL
GROUP BY sch_identifiant, lot_numero, don_lib;
