SELECT sch_identifiant
FROM t_souche 
JOIN t_donneedico AS species ON sch_taxonomie = species.xxx_id
JOIN t_donneedico AS genus ON species.don_parent = genus.don_code
AND genus.don_dic_id = 3755 
JOIN t_donneedico AS country ON sch_lieu = country.xxx_id
JOIN t_milieu_souche
ON t_souche.xxx_id = msc_sch_id
JOIN t_milieu
ON msc_mil_id = t_milieu.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND (genus.don_lib, species.don_lib) IN (SELECT genus_name, sp_epithet FROM taxonomy)
AND sch_temperature_incubation SIMILAR TO '[0-9]+'
AND country.don_lib IN (SELECT name_en FROM world)
GROUP BY sch_identifiant;
