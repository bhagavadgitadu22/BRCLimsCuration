SELECT sch_identifiant 
INTO TEMPORARY TABLE souches_valides
FROM t_souche 
JOIN t_pathogenicite ON sch_pto_id = t_pathogenicite.xxx_id
JOIN t_donneedico AS species ON sch_taxonomie = species.xxx_id
JOIN t_donneedico AS genus ON species.don_parent = genus.don_code
JOIN t_donneedico AS country ON sch_lieu = country.xxx_id
WHERE pto_lib IN ('1', '2', '3', '4')
AND (genus.don_lib, species.don_lib) IN (SELECT genus_name, sp_epithet FROM taxonomy)
AND sch_temperature_incubation SIMILAR TO '[0-9]+'
AND country.don_lib IN (SELECT name_en FROM world)
LIMIT 100;

DELETE FROM t_souche
WHERE sch_identifiant NOT IN (SELECT * FROM souches_valides);