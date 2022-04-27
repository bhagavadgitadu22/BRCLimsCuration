DROP TABLE IF EXISTS ids_mots;

SELECT xxx_id 
INTO ids_mots
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401))
AND sch_mot IS True;

DELETE FROM t_alerte_souche
WHERE als_sch_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_cousinage
USING ids_mots
WHERE sch_id_principal IN (SELECT xxx_id FROM ids_mots)
OR sch_id_secondaire IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_souche_t_carac_phenotypique_resultat
USING ids_mots
WHERE strainentity_xxx_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_carac_phenotypique_resultat
USING ids_mots
WHERE cpr_sch_id IN (SELECT xxx_id FROM ids_mots);

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

DELETE FROM t_sequence
WHERE seq_sch_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_galerieresultat
WHERE gar_gal_id IN (SELECT xxx_id FROM t_galerie
WHERE gal_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_galerie
WHERE gal_sch_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_antibiogrammeresultat
WHERE anr_ant_id IN (SELECT xxx_id FROM t_antibiogramme
WHERE ant_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_antibiogramme
WHERE ant_sch_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_planification
WHERE pla_sch_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM ids_mots);
