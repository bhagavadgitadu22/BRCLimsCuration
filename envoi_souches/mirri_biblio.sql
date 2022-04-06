SELECT btrim(bibli, ' ;,.'), ARRAY_AGG(xxx_id) FROM
(SELECT t_souche.xxx_id, unnest(string_to_array(sch_bibliographie, E'\n')) AS bibli
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False) AS a
WHERE bibli != '' AND LOWER(bibli) NOT LIKE '%submitted%'
GROUP BY bibli
ORDER BY bibli;
