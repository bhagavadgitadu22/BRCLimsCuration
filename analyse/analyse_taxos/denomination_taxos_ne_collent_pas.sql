SELECT sch_identifiant, sch_denomination, path
FROM t_souche
LEFT JOIN chemins_taxonomie
ON t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND path IS NULL;

SELECT sch_denomination, path, LOWER(unaccent(btrim(sch_denomination, '";. :-'))), LOWER(unaccent(btrim(path, '";. :-'))), ARRAY_AGG(sch_identifiant)
FROM t_souche
LEFT JOIN chemins_taxonomie
ON t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND LOWER(unaccent(btrim(sch_denomination, '";. :-'))) NOT SIMILAR TO CONCAT('%', LOWER(unaccent(btrim(path, '";. :-'))), '%')
GROUP BY sch_denomination, path
ORDER BY LOWER(unaccent(sch_denomination)), LOWER(unaccent(path));
