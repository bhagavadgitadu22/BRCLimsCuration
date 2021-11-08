-- rediriger ea1 vers Ea1
UPDATE t_souche
SET sch_patho_animal = 72880
WHERE sch_patho_animal = 167785
AND xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

-- puis on supprime ea1
UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id = 167785
AND don_dic_id IN (SELECT xxx_id FROM t_dico WHERE dic_grp_collection = '[401]')
AND xxx_sup_dat IS NULL;

-- de même pour les riens
UPDATE t_souche
SET sch_patho_animal = NULL
WHERE sch_patho_animal = 73439
AND xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

-- puis on supprime entrée rien
UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id = 73439
AND don_dic_id IN (SELECT xxx_id FROM t_dico WHERE dic_grp_collection = '[401]')
AND xxx_sup_dat IS NULL;
