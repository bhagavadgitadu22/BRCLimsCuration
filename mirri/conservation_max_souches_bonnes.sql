SELECT t_souche.xxx_id
FROM t_souche 
JOIN t_pathogenicite 
ON sch_pto_id = t_pathogenicite.xxx_id
JOIN t_donneedico AS species 
ON sch_taxonomie = species.xxx_id
JOIN t_donneedico AS genus 
ON species.don_parent = genus.don_code
AND genus.don_dic_id = 3755 
JOIN t_donneedico AS country 
ON sch_lieu = country.xxx_id
JOIN t_milieu_souche 
ON t_souche.xxx_id = t_milieu_souche.msc_sch_id
JOIN t_milieu
ON t_milieu.xxx_id = t_milieu_souche.msc_mil_id
JOIN t_donneedico AS conservation
ON sch_conservation = conservation.xxx_id
WHERE pto_lib IN ('1', '2', '3', '4')
AND (genus.don_lib, species.don_lib) IN (SELECT genus_name, sp_epithet FROM taxonomy)
AND sch_temperature_incubation SIMILAR TO '[0-9]+'
AND country.don_lib IN (SELECT name_en FROM world WHERE name_fr != '')
AND conservation.don_lib != 'Stockage Dessicat / Spores'
GROUP BY t_souche.xxx_id
HAVING COUNT(*) = 1;
