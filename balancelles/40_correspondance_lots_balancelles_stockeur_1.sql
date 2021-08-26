DROP TABLE IF EXISTS lots_et_balancelles;

SELECT lot_id, souches_lyophilisees.sch_identifiant, balancelle
INTO TABLE lots_et_balancelles
FROM souches_lyophilisees
JOIN stockeur_1
ON custom_sort(first_strain) <= custom_sort(sch_identifiant) 
AND custom_sort(sch_identifiant) <= custom_sort(last_strain);