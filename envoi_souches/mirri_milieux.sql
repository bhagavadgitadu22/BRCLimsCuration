SELECT mil_numero, mil_designation_en, COUNT(*), ARRAY_AGG(sch_identifiant)
FROM t_milieu
JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
JOIN t_souche
ON t_souche.xxx_id = msc_sch_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY mil_numero, mil_designation_en
ORDER BY mil_numero;
