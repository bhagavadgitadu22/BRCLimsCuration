DROP TABLE IF EXISTS nombre_par_taxos;

SELECT unnest(id_path) AS id_taxo, SUM(somme) AS total
INTO nombre_par_taxos FROM
(SELECT id_path, SUM(CASE WHEN t_souche.xxx_id IS NOT NULL THEN 1 ELSE 0 END) AS somme
FROM chemins_taxonomie
LEFT JOIN t_souche
ON t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
GROUP BY id_path) AS a
GROUP BY unnest(id_path);

/*
SELECT id_taxo, total, path, don_lib
FROM nombre_par_taxos
JOIN chemins_taxonomie
ON sch_taxonomie = id_taxo
WHERE total = 0
ORDER BY path;
*/

UPDATE t_donneedico 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
FROM nombre_par_taxos
WHERE t_donneedico.xxx_id = id_taxo
AND total = 0;
