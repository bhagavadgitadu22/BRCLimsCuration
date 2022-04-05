SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, 
t_cpr_1531.xxx_id AS id_1531, t_cpr_1531.cpr_resultat AS res_1531, t_cpr_1531.cpr_com AS com_1531,
t_cpr_1546.xxx_id AS id_1546, t_cpr_1546.cpr_resultat AS res_1546, t_cpr_1546.cpr_com AS com_1546,
sch_references_equi, sch_historique, sch_dat_isolement, 
sch_isole_a_partir_de, t_origine.don_lib, sch_catalogue,
CASE 
      WHEN t_lot_short.lot_sch_id IS NULL THEN 'false'
      ELSE 'true'
END

FROM t_souche
 
LEFT JOIN (SELECT t_cp_1531.xxx_id, cpr_sch_id, cpr_resultat, cpr_com
FROM t_carac_phenotypique_resultat AS t_cpr_1531
JOIN t_carac_phenotypique AS t_cp_1531
ON t_cp_1531.xxx_id = t_cpr_1531.cpr_cpy_id
AND t_cp_1531.cpy_numero = 1531) AS t_cpr_1531
ON t_souche.xxx_id = t_cpr_1531.cpr_sch_id

LEFT JOIN (SELECT t_cp_1546.xxx_id, cpr_sch_id, cpr_resultat, cpr_com
FROM t_carac_phenotypique_resultat AS t_cpr_1546
JOIN t_carac_phenotypique AS t_cp_1546
ON t_cp_1546.xxx_id = t_cpr_1546.cpr_cpy_id
AND t_cp_1546.cpy_numero = 1546) AS t_cpr_1546
ON t_souche.xxx_id = t_cpr_1546.cpr_sch_id

LEFT JOIN t_donneedico AS t_origine
ON t_origine.xxx_id = t_souche.sch_origine

LEFT JOIN (SELECT DISTINCT lot_sch_id FROM t_lot WHERE xxx_sup_dat IS NULL AND lot_qte_stock != 0) AS t_lot_short
ON t_souche.xxx_id = t_lot_short.lot_sch_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
ORDER BY t_souche.xxx_id;
