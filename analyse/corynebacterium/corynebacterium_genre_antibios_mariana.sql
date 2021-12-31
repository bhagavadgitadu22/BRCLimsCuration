SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_id,

ant_code, ant_dat_realisation, ant_com, don_lib

FROM t_souche
JOIN t_antibiogramme
ON t_souche.xxx_id = ant_sch_id
JOIN t_donneedico AS t_genre
ON ant_genre = t_genre.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM t_souche)
AND sch_denomination LIKE 'Corynebacterium%'

ORDER BY sch_identifiant, sch_version DESC;
