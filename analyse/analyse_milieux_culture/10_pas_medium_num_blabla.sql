SELECT sch_identifiant, 
array_to_string(ARRAY_AGG(DISTINCT mil_numero) FILTER (WHERE t_milieu.xxx_sup_dat IS NULL AND mil_numero IS NOT NULL), E'\n'), 
array_to_string(ARRAY_AGG(DISTINCT mil_designation_fr) FILTER (WHERE t_milieu.xxx_sup_dat IS NULL AND mil_designation_FR IS NOT NULL), E'\n'), 
array_to_string(ARRAY_AGG(DISTINCT mil_designation_en) FILTER (WHERE t_milieu.xxx_sup_dat IS NULL AND mil_designation_en IS NOT NULL), E'\n')
FROM t_souche
LEFT JOIN t_milieu_souche
ON t_souche.xxx_id = msc_sch_id
LEFT JOIN t_milieu
ON msc_mil_id = t_milieu.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
GROUP BY sch_identifiant
ORDER BY sch_identifiant;
