SELECT id_souche, sch_identifiant, arr_ordre, arr_lib FROM 
(SELECT id_souche, sch_identifiant,
ARRAY_AGG(amt_ordre) AS arr_ordre, ARRAY_AGG(don_lib) AS arr_lib, ARRAY_AGG(DISTINCT don_lib) AS arr_lib_uniques
FROM 

(SELECT id_souche, sch_identifiant, amt_ordre, ant_dat_realisation, ant_com, don_lib FROM 

(SELECT DISTINCT ON (sch_identifiant) t_souche.xxx_id AS id_souche, sch_identifiant,

t_antibiogramme.xxx_id AS id_genre, 
ant_code, ant_dat_realisation, ant_com, don_lib AS genre

FROM t_souche
JOIN t_antibiogramme
ON t_souche.xxx_id = ant_sch_id
LEFT JOIN t_donneedico AS t_genre
ON ant_genre = t_genre.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM t_souche)
AND sch_denomination LIKE 'Corynebacterium%'

ORDER BY sch_identifiant, sch_version DESC) AS genre_antibio

LEFT JOIN t_antibiogrammeresultat
ON anr_ant_id = genre_antibio.id_genre
LEFT JOIN t_donneedico
ON anr_resultat = t_donneedico.xxx_id
LEFT JOIN t_antibiogrammemodelegenretest
ON anr_amt_id = t_antibiogrammemodelegenretest.xxx_id

ORDER BY id_souche, amt_ordre) AS a

GROUP BY id_souche, sch_identifiant) AS b

WHERE NOT(array_length(arr_lib_uniques, 1) = 1 AND arr_lib_uniques[0] IS NULL)
