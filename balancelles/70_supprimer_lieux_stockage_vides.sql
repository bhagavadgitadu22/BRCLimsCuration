/*
A voir si je veux supprimer les lieux de stockage inutilisés,
car je pourrais supprimer des lieux utiles même si encore rien dedans (balancelles...)

DROP TABLE IF EXISTS old_lieux_stockage;

SELECT t_lieustockage.xxx_id, lst_nom
INTO TABLE old_lieux_stockage
FROM t_lieustockage
LEFT JOIN t_lot_casestockage
ON t_lieustockage.xxx_id = t_lot_casestockage.lts_lst_id
WHERE t_lot_casestockage.lts_lst_id IS NULL;

DELETE FROM t_lieustockage
WHERE xxx_id IN (SELECT xxx_id FROM old_lieux_stockage);

DROP TABLE IF EXISTS old_lieux_stockage;
*/

DROP TABLE IF EXISTS souches_lyophilisees;
DROP TABLE IF EXISTS stockeur_1;
DROP TABLE IF EXISTS ids_balancelles_1;
DROP TABLE IF EXISTS stockeur_2;
DROP TABLE IF EXISTS ids_balancelles_2;
DROP TABLE IF EXISTS lots_et_balancelles_1;
DROP TABLE IF EXISTS lots_et_balancelles_2;
