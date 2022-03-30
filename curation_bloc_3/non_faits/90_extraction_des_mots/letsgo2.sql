SELECT t_souche.xxx_id, sch_identifiant, sch_version, t_lot.lot_numero, t_lot.lot_numero_generation,
tdd_type.don_lib, tdd_type_stockage.don_lib, 
t_lot.lot_qte_initiale, t_lot.lot_qte_stock, t_lot.lot_qte_minimale, t_lot.lot_date_creation, t_lot.lot_com, 
tdd_unite.don_lib, t_lot2.lot_numero, 
t_lot.lot_en_vente, 
tdd_emballage_primaire.don_lib, tdd_solide_liquide.don_lib, tdd_support_conservation.don_lib,
t_lot.xxx_cre_dat, t_lot.xxx_maj_dat, t_lot.xxx_sup_dat
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
LEFT JOIN t_donneedico AS tdd_type
ON lot_type = tdd_type.xxx_id
LEFT JOIN t_donneedico AS tdd_type_stockage
ON lot_type_stockage = tdd_type_stockage.xxx_id
LEFT JOIN t_donneedico AS tdd_unite
ON lot_unite = tdd_unite.xxx_id
LEFT JOIN t_lot AS t_lot2
ON t_lot.lot_src_lot_id = t_lot2.xxx_id
LEFT JOIN t_donneedico AS tdd_emballage_primaire
ON t_lot.lot_emballage_primaire = tdd_emballage_primaire.xxx_id
LEFT JOIN t_donneedico AS tdd_solide_liquide
ON t_lot.lot_solide_liquide = tdd_solide_liquide.xxx_id
LEFT JOIN t_donneedico AS tdd_support_conservation
ON t_lot.lot_support_conservation = tdd_support_conservation.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, xxx_cre_dat, xxx_maj_dat, xxx_sup_dat,
sch_identifiant, sch_version, t_lot.lot_numero,
cmd_dat, cmd_code, clt_code, tdd_article.don_lib, 
acm_numero, acm_quantite, acm_prix, acm_denomination, acm_repiquee, acm_com
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_article_commande
ON acm_lot_id = t_lot.xxx_id
LEFT JOIN t_commande
ON acm_cmd_id = t_commande.xxx_id
LEFT JOIN t_client
ON cmd_clt_id = t_client.xxx_id
LEFT JOIN t_donneedico AS tdd_article
ON acm_article = tdd_article.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, xxx_cre_dat, xxx_maj_dat, xxx_sup_dat,
sch_identifiant, sch_version, t_lot.lot_numero,
cql_code, tdd_phase.don_lib, tdd_controle.don_lib, 
cql_valeur_attendue, cql_valeur_obtenue, tdd_resultat.don_lib,
cql_operateur, cql_date_debut, cql_date_fin, cql_com
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_controlequalite_lot
ON cql_lot_id = t_lot.xxx_id
LEFT JOIN t_donneedico AS tdd_phase
ON cql_phase = tdd_phase.xxx_id
LEFT JOIN t_donneedico AS tdd_controle
ON cql_controle = tdd_controle.xxx_id
LEFT JOIN t_donneedico AS tdd_resultat
ON cql_resultat = tdd_resultat.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, xxx_cre_dat, xxx_maj_dat, xxx_sup_dat,
sch_identifiant, sch_version, t_lot.lot_numero,
mvt_code, mvt_quantite, tdd_motif.don_lib
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_mouvementstock
ON mvt_lot_id = t_lot.xxx_id
LEFT JOIN t_donneedico AS tdd_motif
ON mvt_motif = tdd_motif.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, sch_identifiant, sch_version, t_lot.lot_numero,
lst_nom, lst_type, cst_numero, cst_pos_x, cst_pos_y
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_lot_casestockage
ON lts_lot_id = t_lot.xxx_id
JOIN t_casestockage
ON t_casestockage.xxx_id = lts_cst_id
JOIN t_lieustockage
ON t_lieustockage.xxx_id = lts_lst_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, sch_identifiant, sch_version, t_lot.lot_numero,
--mil_numero, mil_designation_fr, mil_designation_en,
tdd_type_action.don_lib, pla_action, pla_dat_previ, pla_dat_realisation,
tdd_type_produit.don_lib, pla_remarque, pla_action_terminee, 
CONCAT(usr_prenom, ' ', usr_nom)
FROM t_souche
JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
JOIN t_planification
ON pla_lot_id = t_lot.xxx_id
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

DELETE FROM t_mouvementstock
WHERE mvt_lot_id IN (SELECT xxx_id FROM t_lot
WHERE lot_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_lot_casestockage
WHERE lts_lot_id IN (SELECT xxx_id FROM t_lot
WHERE lot_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_planification
WHERE pla_lot_id IN (SELECT xxx_id FROM t_lot
WHERE lot_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_controlequalite_lot
WHERE cql_lot_id IN (SELECT xxx_id FROM t_lot
WHERE lot_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_article_commande
WHERE acm_lot_id IN (SELECT xxx_id FROM t_lot
WHERE lot_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_lot
WHERE lot_sch_id IN (SELECT xxx_id FROM ids_mots);
