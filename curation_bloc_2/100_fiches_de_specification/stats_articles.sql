SELECT sch_identifiant, lot_numero, type_lot, acm_lot_id, ARRAY_AGG(DISTINCT acm_article), ARRAY_AGG(DISTINCT don_lib)
FROM t_article_commande 
JOIN t_donneedico 
ON t_donneedico.xxx_id = acm_article
JOIN articles_fiches_a_supprimer
ON articles_fiches_a_supprimer.lot_id = acm_lot_id
GROUP BY sch_identifiant, lot_numero, type_lot, acm_lot_id;
