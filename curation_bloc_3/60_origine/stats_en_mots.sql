SELECT don_lib, LOWER(word), COUNT(*)
FROM (SELECT don_lib, unnest(string_to_array(sch_isole_a_partir_de, ' ')) AS word
FROM t_souche
LEFT JOIN t_donneedico
ON t_donneedico.xxx_id = sch_origine
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)) AS a
GROUP BY don_lib, LOWER(word)
ORDER BY don_lib, -COUNT(*);
