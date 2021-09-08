SELECT t_milieu.xxx_id, mil_designation_en
FROM t_milieu
LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id
WHERE t_souche.xxx_id IS NULL
GROUP BY t_milieu.xxx_id, mil_designation_en
ORDER BY mil_designation_en;
