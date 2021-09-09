-- on sélectionne les lots lyophylisées de la cip
DROP TABLE IF EXISTS souches_lyophilisees;

SELECT t_lot.xxx_id AS lot_id, sch_identifiant, t_lieustockage.xxx_id AS stockage_id, lst_nom
INTO TABLE souches_lyophilisees
FROM t_lot

JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
JOIN t_donneedico
ON t_donneedico.xxx_id = lot_type_stockage

LEFT JOIN t_lot_casestockage
ON t_lot.xxx_id = t_lot_casestockage.lts_lot_id
LEFT JOIN t_lieustockage
ON t_lieustockage.xxx_id = t_lot_casestockage.lts_lst_id

WHERE don_lib = 'Stockage Lyophilisat'
AND (sch_identifiant SIMILAR TO 'CIP A[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{2}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{1}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP 1[0-9]{5}T?')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);
