SELECT DISTINCT sch_denomination
FROM last_version_souches_cip
ORDER BY sch_denomination;

SELECT sch_denomination, COUNT(*)
FROM last_version_souches_cip
LEFT JOIN souches_types_de_souches_short
ON sch_denomination = denom
WHERE denom IS NULL
GROUP BY sch_denomination
ORDER BY COUNT(*) DESC;
