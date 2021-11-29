SELECT sch_identifiant, COUNT(*), (REGEXP_MATCH(sch_references_equi, 'WDCM ?([0-9]+)'))[1]
FROM t_commande
JOIN t_client
ON cmd_clt_id = t_client.xxx_id
JOIN t_donneedico
ON t_donneedico.xxx_id = clt_code_tarif
JOIN t_article_commande
ON t_commande.xxx_id = acm_cmd_id
JOIN t_lot
ON acm_lot_id = t_lot.xxx_id
JOIN t_souche
ON lot_sch_id = t_souche.xxx_id
WHERE EXTRACT(YEAR FROM cmd_dat) > 2010
GROUP BY (REGEXP_MATCH(sch_references_equi, 'WDCM ?([0-9]+)'))[1], sch_identifiant
ORDER BY -COUNT(*)