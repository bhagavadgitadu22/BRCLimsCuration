DROP TABLE IF EXISTS new_taxos;

-- maintenant que les nouvelles taxos ont été créée on peut mettre à jour le champ taxnomie
SELECT denoms_sans_taxos.xxx_id AS sch_id, 
chemins_taxonomie.sch_taxonomie AS path_id, 
short_denom, path
INTO new_taxos
FROM denoms_sans_taxos
JOIN chemins_taxonomie
ON short_denom = path;

UPDATE t_souche
SET sch_taxonomie = path_id
FROM new_taxos
WHERE t_souche.xxx_id = sch_id;

-- ce qu'il manque encore
/*
SELECT *
FROM denoms_sans_taxos
LEFT JOIN chemins_taxonomie
ON short_denom = path
WHERE path IS NULL;
*/
