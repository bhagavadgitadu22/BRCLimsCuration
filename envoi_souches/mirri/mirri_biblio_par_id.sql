DROP TABLE IF EXISTS biblios_par_id;

SELECT xxx_id, bibli 
INTO TABLE biblios_par_id
FROM (SELECT t_souche.xxx_id, unnest(regexp_split_to_array(sch_bibliographie, E'[\\n\\r]+')) AS bibli
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False) AS a
WHERE bibli != '' AND LOWER(bibli) NOT LIKE '%submitted%';
