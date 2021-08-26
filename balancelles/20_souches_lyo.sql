DROP TABLE IF EXISTS souches_lyophilisees;

SELECT t_lot.xxx_id AS lot_id, sch_identifiant 
INTO TABLE souches_lyophilisees
FROM t_lot
JOIN t_souche
ON t_souche.xxx_id = t_lot.lot_sch_id
JOIN t_donneedico
ON t_donneedico.xxx_id = lot_type_stockage
WHERE don_lib = 'Stockage Lyophilisat';
