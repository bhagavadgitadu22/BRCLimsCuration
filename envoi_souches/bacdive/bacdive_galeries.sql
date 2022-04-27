SELECT t_souche.xxx_id, sch_identifiant,
t_donneedico.don_lib AS gal_type, gal_dat_realisation, gal_com, 
gtt_ordre, tddtest.don_lib, 
tdd_lecture1.don_lib, tdd_lecture2.don_lib, gar_resultat
FROM t_souche
JOIN t_galerie
ON gal_sch_id = t_souche.xxx_id
LEFT JOIN t_donneedico
ON gal_type = t_donneedico.xxx_id
LEFT JOIN t_galerieresultat
ON gar_gal_id = t_galerie.xxx_id
LEFT JOIN t_galeriemodeletypetest
ON gar_gtt_id = t_galeriemodeletypetest.xxx_id
LEFT JOIN t_galeriemodeletype
ON gtt_gmt_id = t_galeriemodeletype.xxx_id
LEFT JOIN t_donneedico AS tddtype
ON gmt_type = tddtype.xxx_id
LEFT JOIN t_donneedico AS tddtest
ON gtt_test = tddtest.xxx_id
LEFT JOIN t_donneedico AS tdd_lecture1
ON gar_premiere_lecture = tdd_lecture1.xxx_id
LEFT JOIN t_donneedico AS tdd_lecture2
ON gar_seconde_lecture = tdd_lecture2.xxx_id

WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
ORDER BY t_souche.xxx_id, gal_type, gtt_ordre;
