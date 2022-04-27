SELECT btrim(bibli, ' ;,.'), array_to_string(ARRAY_AGG(xxx_id), ','), array_to_string(ARRAY_AGG(sch_identifiant), ',') FROM
(SELECT t_souche.xxx_id, t_souche.sch_identifiant, unnest(regexp_split_to_array(sch_bibliographie, E'[\\n\\r]+')) AS bibli
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False) AS a
WHERE bibli != '' AND LOWER(bibli) NOT LIKE '%submitted%'
GROUP BY bibli
ORDER BY bibli;
