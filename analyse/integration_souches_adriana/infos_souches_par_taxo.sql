SELECT sch_denomination, COUNT(*), ARRAY_AGG(sch_identifiant)
FROM (SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, 
sch_references_equi, sch_historique, sch_dat_isolement, 
sch_isole_a_partir_de, sch_catalogue,
CASE 
      WHEN t_lot_short.lot_sch_id IS NULL THEN 'false'
      ELSE 'true'
END AS presence_lot
FROM t_souche
LEFT JOIN (SELECT DISTINCT lot_sch_id FROM t_lot WHERE xxx_sup_dat IS NULL AND lot_qte_stock != 0) AS t_lot_short
ON t_souche.xxx_id = t_lot_short.lot_sch_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
ORDER BY t_souche.xxx_id) AS a
WHERE presence_lot = 'false'
AND LOWER(sch_denomination) NOT LIKE '%pas de souche%'
GROUP BY sch_denomination
ORDER BY COUNT(*) DESC;
