SELECT sch_identifiant, array_to_string(ARRAY_AGG(DISTINCT sch_catalogue), ', '), COUNT(*)
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_article_commande
ON acm_lot_id = t_lot.xxx_id
JOIN t_commande
ON t_commande.xxx_id = acm_cmd_id
WHERE t_souche.xxx_id IN (SELECT xxx_id from souches_groupe_cip)
GROUP BY sch_identifiant
ORDER BY COUNT(*) DESC;

-- quand count(*) indique plusieurs en théorie ça indique juste que plusieurs versions de la souche
-- attention néanmoins à d'abord ne garder qu'une version de chaque souche avant de faire mon tri sinon ça n'a juste pas de sens
SELECT sch_identifiant, COUNT(*)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id from souches_groupe_cip)
AND sch_identifiant NOT IN
(SELECT sch_identifiant
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_article_commande
ON acm_lot_id = t_lot.xxx_id
JOIN t_commande
ON t_commande.xxx_id = acm_cmd_id
WHERE t_souche.xxx_id IN (SELECT xxx_id from souches_groupe_cip)
AND EXTRACT(YEAR FROM cmd_dat) > 2010
GROUP BY sch_identifiant)
GROUP BY sch_identifiant;

SELECT DISTINCT sch_identifiant
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id from souches_groupe_cip);

