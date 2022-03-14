SELECT LOWER(word), COUNT(*)
FROM (SELECT unnest(string_to_array(sch_isole_a_partir_de, ' ')) AS word
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL) AS a
GROUP BY LOWER(word)
ORDER BY COUNT(*) DESC;
