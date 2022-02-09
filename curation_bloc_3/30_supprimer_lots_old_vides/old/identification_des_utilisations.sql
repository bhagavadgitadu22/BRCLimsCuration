DROP TABLE IF EXISTS articles_fiches_a_supprimer;

SELECT t_souche.xxx_id AS sch_id, t_lot.xxx_id AS lot_id, 
sch_identifiant, lot_numero, type_lot.don_lib AS type_lot, 
type_article.don_lib AS type_article,
t_article_commande.xxx_id AS art_cmd_id, acm_article, 
type_article.xxx_id AS elmt_dico_id
INTO TABLE articles_fiches_a_supprimer
FROM t_article_commande 
JOIN t_donneedico AS type_article
ON type_article.xxx_id = acm_article 
JOIN t_lot
ON t_lot.xxx_id = acm_lot_id
JOIN t_donneedico AS type_lot
ON lot_type = type_lot.xxx_id
JOIN t_souche
ON t_souche.xxx_id = lot_sch_id
WHERE LOWER(type_article.don_lib) LIKE '%spécification%'
AND t_lot.xxx_sup_dat IS NULL
AND t_souche.xxx_sup_dat IS NULL;

UPDATE t_article_commande
SET acm_article = 3742
FROM articles_fiches_a_supprimer
WHERE art_cmd_id = t_article_commande.xxx_id;

UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
FROM articles_fiches_a_supprimer
WHERE elmt_dico_id = t_donneedico.xxx_id;
