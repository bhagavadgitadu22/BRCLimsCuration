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

SELECT t_souche.xxx_id, sch_identifiant, sch_version, don_lib 
FROM t_souche
JOIN t_alerte_souche
ON als_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON als_alerte = t_donneedico.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
AND t_souche.xxx_id NOT IN (SELECT xxx_id FROM last_version_souches_cip)
ORDER BY t_souche.xxx_id;

DELETE FROM t_alerte_souche
WHERE als_sch_id IN (SELECT xxx_id FROM ids_mots);

SELECT ta.xxx_id, ta.sch_identifiant, ta.sch_version, tb.xxx_id, tb.sch_identifiant, tb.sch_version, don_lib 
FROM t_cousinage
JOIN t_souche AS ta
ON sch_id_principal = ta.xxx_id
JOIN t_souche AS tb
ON sch_id_secondaire = tb.xxx_id
JOIN t_donneedico
ON cou_type = t_donneedico.xxx_id
WHERE (ta.sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND ta.sch_mot IS True)
OR (tb.sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND tb.sch_mot IS True)
ORDER BY ta.xxx_id;

DELETE FROM t_cousinage
USING ids_mots
WHERE sch_id_principal IN (SELECT xxx_id FROM ids_mots)
OR sch_id_secondaire IN (SELECT xxx_id FROM ids_mots);

SELECT t_souche.xxx_id, sch_identifiant, sch_version, don_lib, cpy_numero, cpy_methode, cpr_resultat, cpr_com,
t_carac_phenotypique_resultat.xxx_cre_dat, t_carac_phenotypique_resultat.xxx_maj_dat, t_carac_phenotypique_resultat.xxx_sup_dat
FROM t_souche_t_carac_phenotypique_resultat
JOIN t_souche
ON strainentity_xxx_id = t_souche.xxx_id
JOIN t_carac_phenotypique_resultat
ON phenotypiccaracteristicresult_xxx_id = t_carac_phenotypique_resultat.xxx_id
JOIN t_carac_phenotypique
ON t_carac_phenotypique.xxx_id = cpr_cpy_id
JOIN t_donneedico
ON cpy_id = t_donneedico.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

DELETE FROM t_souche_t_carac_phenotypique_resultat
USING ids_mots
WHERE strainentity_xxx_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_carac_phenotypique_resultat
USING ids_mots
WHERE cpr_sch_id IN (SELECT xxx_id FROM ids_mots);

SELECT t_souche.xxx_id, 
sch_identifiant, sch_version, don_lib, seq_sequence, seq_blast, seq_qualite, seq_lien_base_publique, seq_com
--, tsp_id, tsp_sequence
FROM t_souche
JOIN t_sequence
ON seq_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON seq_type = t_donneedico.xxx_id
--LEFT JOIN t_sequenceprimer
--ON spr_seq_id = t_sequence.xxx_id
--LEFT JOIN t_typesequence_primer
--ON spr_tsp_id = t_typesequence_primer.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

DELETE FROM t_sequence
WHERE seq_sch_id IN (SELECT xxx_id FROM ids_mots);

SELECT t_souche.xxx_id,
sch_identifiant, sch_version, 
t_donneedico.don_lib, gal_dat_realisation, gal_com, 
gtt_ordre, tddtest.don_lib, gar_resultat, 
tdd2.don_lib, tdd3.don_lib
FROM t_souche
JOIN t_galerie
ON gal_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON gal_type = t_donneedico.xxx_id
JOIN t_galerieresultat
ON gar_gal_id = t_galerie.xxx_id
JOIN t_galeriemodeletypetest
ON gar_gtt_id = t_galeriemodeletypetest.xxx_id
JOIN t_donneedico AS tdd2
ON gar_premiere_lecture = tdd2.xxx_id
JOIN t_donneedico AS tdd3
ON gar_seconde_lecture = tdd3.xxx_id
JOIN t_galeriemodeletype
ON gtt_gmt_id = t_galeriemodeletype.xxx_id
JOIN t_donneedico AS tddtype
ON gmt_type = tddtype.xxx_id
JOIN t_donneedico AS tddtest
ON gtt_test = tddtest.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

DELETE FROM t_galerieresultat
WHERE gar_gal_id IN (SELECT xxx_id FROM t_galerie
WHERE gal_sch_id IN (SELECT xxx_id FROM ids_mots));

SELECT t_souche.xxx_id,
sch_identifiant, sch_version, 
t_donneedico.don_lib, ant_dat_realisation, ant_com,
amt_ordre, tddtest.don_lib AS amt_test,
tddres.don_lib AS anr_resultat, anr_diametre
FROM t_souche
JOIN t_antibiogramme
ON ant_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON ant_genre = t_donneedico.xxx_id
JOIN t_antibiogrammeresultat
ON anr_ant_id = t_antibiogramme.xxx_id
JOIN t_antibiogrammemodelegenretest
ON anr_amt_id = t_antibiogrammemodelegenretest.xxx_id
JOIN t_antibiogrammemodelegenre
ON amt_amg_id = t_antibiogrammemodelegenre.xxx_id
JOIN t_donneedico AS tddgenre
ON amg_genre = tddgenre.xxx_id
JOIN t_donneedico AS tddtest
ON amt_test = tddtest.xxx_id
JOIN t_donneedico AS tddres
ON anr_resultat = tddres.xxx_id
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_mot IS True
ORDER BY t_souche.xxx_id;

DELETE FROM t_antibiogrammeresultat
WHERE anr_ant_id IN (SELECT xxx_id FROM t_antibiogramme
WHERE ant_sch_id IN (SELECT xxx_id FROM ids_mots));

DELETE FROM t_antibiogramme
WHERE ant_sch_id IN (SELECT xxx_id FROM ids_mots);
