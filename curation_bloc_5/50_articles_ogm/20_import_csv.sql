DROP TABLE IF EXISTS ids_souches;

COPY articles_ogm_par_erreur (identifier)
FROM 'C:/Users/Public/Documents/articles_ogm_par_erreur.csv'
DELIMITER ';';

DELETE FROM articles_ogm_par_erreur WHERE identifier = '';

SELECT xxx_id
INTO ids_souches
FROM t_souche
JOIN articles_ogm_par_erreur
ON identifier = sch_identifiant;
