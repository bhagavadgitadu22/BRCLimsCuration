SELECT sch_identifiant, sch_denomination, sch_catalogue, sch_ogm, don_lib
FROM t_souche
LEFT JOIN t_article_souche  ON ars_sch_id = t_souche.xxx_id
LEFT JOIN t_donneedico ON ars_article = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND (don_lib = 'OGM'
OR (don_lib IS NULL AND sch_ogm IS True));
