SELECT sch.sch_identifiant, sch.sch_denomination, type_sch.sch_identifiant, type_sch.sch_denomination
FROM last_version_souches_cip AS sch
LEFT JOIN last_version_souches_cip AS type_sch
ON sch.sch_denomination = type_sch.sch_denomination
AND sch.sch_identifiant != type_sch.sch_identifiant
AND type_sch.sch_identifiant LIKE '%T'
WHERE sch.sch_identifiant NOT LIKE '%T'
AND type_sch.sch_identifiant IS NULL
ORDER BY type_sch.sch_identifiant DESC;
