SELECT id_souche, sch_identifiant, sch_denomination,
lieu_origine, sch_isole_a_partir_de,
date_prelevement, date_isolement, sch_bibliographie, sch_proprietes, 
ARRAY_AGG(nom_antibio) AS antibios, 
ARRAY_AGG(resultat) AS resultats,
ARRAY_AGG(anr_diametre) AS diametres

FROM 
(SELECT id_souche, sch_identifiant, sch_denomination,
lieu_origine, sch_isole_a_partir_de,
EXTRACT(YEAR FROM sch_dat_prelevement) AS date_prelevement, 
EXTRACT(YEAR FROM sch_dat_isolement) AS date_isolement,
sch_bibliographie, sch_proprietes,
id_genre, nom_antibio.don_lib AS nom_antibio, 
anr_diametre, t_resultat.don_lib AS resultat
FROM 

(SELECT last_version_souches_cip.xxx_id AS id_souche, 
sch_identifiant, sch_denomination,
lieu_origine, sch_isole_a_partir_de,
sch_dat_prelevement, sch_dat_isolement, 
sch_bibliographie, sch_proprietes,
t_antibiogramme.xxx_id AS id_genre, 
ant_code, ant_dat_realisation, ant_com, don_lib AS genre

FROM last_version_souches_cip
LEFT JOIN t_antibiogramme
ON last_version_souches_cip.xxx_id = ant_sch_id
LEFT JOIN t_donneedico AS t_genre
ON ant_genre = t_genre.xxx_id

WHERE sch_denomination SIMILAR TO 'Corynebacterium%') AS genre_antibio

LEFT JOIN t_antibiogrammeresultat
ON anr_ant_id = genre_antibio.id_genre
LEFT JOIN t_donneedico AS t_resultat
ON anr_resultat = t_resultat.xxx_id
LEFT JOIN t_antibiogrammemodelegenretest
ON anr_amt_id = t_antibiogrammemodelegenretest.xxx_id
LEFT JOIN t_donneedico AS nom_antibio
ON nom_antibio.xxx_id = amt_test) AS a

GROUP BY id_souche, sch_identifiant, sch_denomination, lieu_origine, sch_isole_a_partir_de, date_prelevement, date_isolement, sch_bibliographie, sch_proprietes
ORDER BY id_souche;
