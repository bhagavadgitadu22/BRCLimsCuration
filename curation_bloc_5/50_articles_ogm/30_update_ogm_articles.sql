/*
SELECT ars_article, (SELECT DISTINCT ars_article FROM t_article_souche
LEFT JOIN t_donneedico ON ars_article = t_donneedico.xxx_id
WHERE don_lib = 'Souches Bacteriennes Classe 1 et 2')
FROM t_article_souche
JOIN ids_souches
ON ars_sch_id = ids_souches.xxx_id;
*/

UPDATE t_article_souche
SET ars_article = (SELECT DISTINCT ars_article FROM t_article_souche
LEFT JOIN t_donneedico ON ars_article = t_donneedico.xxx_id
WHERE don_lib = 'Souches Bacteriennes Classe 1 et 2')
FROM ids_souches
WHERE ars_sch_id = ids_souches.xxx_id;
