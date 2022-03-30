SELECT t_souche.xxx_id, sch_identifiant, sch_version, t_lot.lot_numero,
--mil_numero, mil_designation_fr, mil_designation_en,
tdd_type_action.don_lib, pla_action, pla_dat_previ, pla_dat_realisation,
tdd_type_produit.don_lib, pla_remarque, pla_action_terminee, 
CONCAT(usr_prenom, ' ', usr_nom)
FROM t_souche
LEFT JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_planification
ON pla_sch_id = t_souche.xxx_id
--LEFT JOIN t_milieu
--ON pla_mil_id = t_milieu.xxx_id
--LEFT JOIN t_lotmilieu
--ON pla_lom_id = t_lotmilieu.xxx_id
LEFT JOIN t_donneedico AS tdd_type_action
ON tdd_type_action.xxx_id = pla_type_action
LEFT JOIN t_donneedico AS tdd_type_produit
ON tdd_type_produit.xxx_id = pla_type_produit
LEFT JOIN t_utilisateur
ON pla_usr_id = t_utilisateur.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;
