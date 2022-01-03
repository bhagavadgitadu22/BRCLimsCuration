SELECT sch.sch_identifiant, ARRAY_AGG(sch.sch_denomination), ARRAY_AGG(type_sch.sch_identifiant), ARRAY_AGG(type_sch.sch_denomination)
FROM t_souche AS sch
LEFT JOIN t_souche AS type_sch
ON sch.sch_denomination = type_sch.sch_denomination
WHERE sch.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND type_sch.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch.sch_identifiant != type_sch.sch_identifiant
AND type_sch.sch_identifiant LIKE '%T'
GROUP BY sch.sch_identifiant
HAVING COUNT(*) > 1;
