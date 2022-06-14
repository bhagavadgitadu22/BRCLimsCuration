SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, 
sch_references_equi, reverse(split_part(reverse(sch_autres_coll), ';', 1)),
sch_historique, t_deposant.don_lib, 
sch_dat_isolement, t_atm.don_lib,
sch_isole_a_partir_de, t_origine.don_lib, t_lieu.don_lib, sch_lieu_precis, 
sch_catalogue,
CASE 
      WHEN t_lot_short.lot_sch_id IS NULL THEN 'false'
      ELSE 'true'
END

FROM t_souche
LEFT JOIN t_donneedico AS t_deposant
ON t_deposant.xxx_id = t_souche.sch_depositaire
LEFT JOIN t_donneedico AS t_origine
ON t_origine.xxx_id = t_souche.sch_origine
LEFT JOIN t_donneedico AS t_lieu
ON t_lieu.xxx_id = t_souche.sch_lieu
LEFT JOIN t_donneedico AS t_atm
ON t_atm.xxx_id = t_souche.sch_atmosphere_incubation
LEFT JOIN (SELECT DISTINCT lot_sch_id FROM t_lot WHERE xxx_sup_dat IS NULL AND lot_qte_stock != 0) AS t_lot_short
ON t_souche.xxx_id = t_lot_short.lot_sch_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
ORDER BY t_souche.xxx_id;
