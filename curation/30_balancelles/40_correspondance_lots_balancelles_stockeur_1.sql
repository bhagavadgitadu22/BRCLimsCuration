-- on garde l'endroit où est stocké chaque lot de lyo et l'endroit où il devrait être
DROP TABLE IF EXISTS lots_et_balancelles_1;

SELECT lot_id, sch_identifiant, 
old_id_balancelle, balancelle, id_balancelle,
max, ROW_NUMBER() OVER (PARTITION BY balancelle) AS nb_row
INTO TABLE lots_et_balancelles_1

FROM (SELECT lot_id, sch_identifiant, 
old_id_balancelle, balancelle, id_balancelle,
MAX(lts_cst_id) AS max

FROM (SELECT lot_id, souches_lyophilisees.sch_identifiant, 
souches_lyophilisees.stockage_id AS old_id_balancelle, balancelle, 
ids_balancelles_1.xxx_id AS id_balancelle
FROM souches_lyophilisees
JOIN stockeur_1
ON custom_sort(first_strain) <= custom_sort(sch_identifiant) 
AND custom_sort(sch_identifiant) <= custom_sort(last_strain)
JOIN ids_balancelles_1
ON ids_balancelles_1.lst_nom = CONCAT('Balancelle-', balancelle)
WHERE CONCAT('Balancelle-', balancelle) != souches_lyophilisees.lst_nom) AS a

JOIN t_lot_casestockage
ON lts_lst_id = id_balancelle
GROUP BY lot_id, sch_identifiant, old_id_balancelle, balancelle, id_balancelle) AS b;
