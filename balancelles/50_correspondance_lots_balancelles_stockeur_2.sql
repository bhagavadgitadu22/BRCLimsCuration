DROP TABLE IF EXISTS lots_et_balancelles;

SELECT lot_id, souches_lyophilisees.sch_identifiant, 
souches_lyophilisees.lst_nom AS old_balancelle, balancelle, 
ids_balancelles_2.xxx_id AS id_balancelle
INTO TABLE lots_et_balancelles
FROM souches_lyophilisees
JOIN stockeur_2
ON custom_sort(first_strain) <= custom_sort(sch_identifiant) 
AND custom_sort(sch_identifiant) <= custom_sort(last_strain)
JOIN ids_balancelles_2
ON ids_balancelles_2.lst_nom = CONCAT('Balancelle-', balancelle);
