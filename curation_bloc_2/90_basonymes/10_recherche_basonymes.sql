SELECT sch.sch_identifiant, type_sch.sch_identifiant,
sch.basonyme, type_sch.basonyme,
denom
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.basonyme != type_sch.basonyme;

SELECT sch.sch_identifiant, type_sch.sch_identifiant,
sch.basonyme, type_sch.basonyme,
denom
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.basonyme IS NULL AND type_sch.basonyme IS NOT NULL;
