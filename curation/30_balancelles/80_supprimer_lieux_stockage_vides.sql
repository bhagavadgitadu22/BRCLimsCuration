-- supprimer les lieux de stockage inutilisés
DROP TABLE IF EXISTS old_lieux_stockage;

SELECT lieu, lst_nom
INTO TABLE old_lieux_stockage
FROM differents_rangements
LEFT JOIN t_lot_casestockage
ON lieu = t_lot_casestockage.lts_lst_id
WHERE t_lot_casestockage.lts_lst_id IS NULL
AND n_utilisations = 1
AND (lieu IN (SELECT DISTINCT old_id_balancelle FROM lots_et_balancelles_1)
OR lieu IN (SELECT DISTINCT old_id_balancelle FROM lots_et_balancelles_2));

UPDATE t_lieustockage
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (SELECT lieu FROM old_lieux_stockage);
