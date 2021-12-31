SELECT sch_identifiant, (REGEXP_MATCHES(sch_references_equi, 'WDCM ?([0-9]+)'))[1], array_length(array_remove(array_agg(t_commande.xxx_id), NULL), 1)
FROM t_souche
LEFT JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
LEFT JOIN t_article_commande
ON acm_lot_id = t_lot.xxx_id
LEFT JOIN t_commande
ON t_commande.xxx_id = acm_cmd_id