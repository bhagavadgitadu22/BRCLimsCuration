DROP TABLE IF EXISTS last_forever_years;
DROP TABLE IF EXISTS last_ten_years;

SELECT sch_identifiant, array_to_string(ARRAY_AGG(DISTINCT sch_catalogue), ', '), COUNT(*) AS count_forever
INTO last_forever_years
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

SELECT sch_identifiant, array_to_string(ARRAY_AGG(DISTINCT sch_catalogue), ', '), COUNT(*) AS count_ten
INTO last_ten_years
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_article_commande
ON acm_lot_id = t_lot.xxx_id
JOIN t_commande
ON t_commande.xxx_id = acm_cmd_id
WHERE t_souche.xxx_id IN (SELECT xxx_id from souches_groupe_cip)
AND EXTRACT(YEAR FROM cmd_dat) > 2010
GROUP BY sch_identifiant
ORDER BY COUNT(*) DESC;

SELECT last_version_souches_cip.sch_identifiant, 
sch_denomination, count_forever, count_ten,
CASE WHEN sch_catalogue IS True THEN 'Yes'
	ELSE 'No'
END AS catalogue,
CASE WHEN t_1546.xxx_id IS NULL THEN 'No'
	ELSE 'Yes'
END AS genome,
t_1546.cpr_com
FROM last_version_souches_cip

LEFT JOIN last_forever_years
ON last_version_souches_cip.sch_identifiant = last_forever_years.sch_identifiant
LEFT JOIN last_ten_years
ON last_version_souches_cip.sch_identifiant = last_ten_years.sch_identifiant

LEFT JOIN (SELECT t_cp.xxx_id, cpr_sch_id, cpr_com
FROM t_carac_phenotypique_resultat AS t_cpr
JOIN t_carac_phenotypique AS t_cp
ON t_cp.xxx_id = t_cpr.cpr_cpy_id
AND t_cp.cpy_numero = 1546) AS t_1546
ON last_version_souches_cip.xxx_id = t_1546.cpr_sch_id;
