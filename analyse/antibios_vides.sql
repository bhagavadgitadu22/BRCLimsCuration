SELECT t_souche.xxx_id, sch_identifiant,
t_donneedico.don_lib AS genre_antibio, ant_dat_realisation, ant_com,
amt_ordre, tddtest.don_lib AS amt_test,
tddres.don_lib AS anr_resultat, anr_diametre
FROM t_souche
JOIN t_antibiogramme
ON ant_sch_id = t_souche.xxx_id
LEFT JOIN t_donneedico
ON ant_genre = t_donneedico.xxx_id
LEFT JOIN t_antibiogrammeresultat
ON anr_ant_id = t_antibiogramme.xxx_id
LEFT JOIN t_antibiogrammemodelegenretest
ON anr_amt_id = t_antibiogrammemodelegenretest.xxx_id
LEFT JOIN t_antibiogrammemodelegenre
ON amt_amg_id = t_antibiogrammemodelegenre.xxx_id
LEFT JOIN t_donneedico AS tddgenre
ON amg_genre = tddgenre.xxx_id
LEFT JOIN t_donneedico AS tddtest
ON amt_test = tddtest.xxx_id
LEFT JOIN t_donneedico AS tddres
ON anr_resultat = tddres.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_mot IS False
AND anr_resultat IS NULL AND anr_diametre = ''
ORDER BY t_souche.xxx_id, t_donneedico.don_lib, amt_ordre;
