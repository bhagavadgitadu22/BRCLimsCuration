SELECT sch_isole_a_partir_de, COUNT(*), array_to_string(ARRAY_AGG(CONCAT(sch_identifiant, ' version ', sch_version)), ', '), ARRAY_AGG(xxx_id)
FROM last_version_souches_cip
WHERE sch_origine IS NULL
AND sch_isole_a_partir_de != ''
--AND sch_catalogue IS True
GROUP BY sch_isole_a_partir_de
ORDER BY sch_isole_a_partir_de;

SELECT COUNT(*)
FROM last_version_souches_cip
WHERE sch_origine IS NULL
AND sch_isole_a_partir_de != ''
--AND sch_catalogue IS True;
