SELECT t_souche.xxx_id,
sch_identifiant, sch_version, 
t_donneedico.don_lib, gal_dat_realisation, gal_com, 
gtt_ordre, tddtest.don_lib, gar_resultat, 
tdd2.don_lib, tdd3.don_lib
FROM t_souche
JOIN t_galerie
ON gal_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON gal_type = t_donneedico.xxx_id
JOIN t_galerieresultat
ON gar_gal_id = t_galerie.xxx_id
JOIN t_galeriemodeletypetest
ON gar_gtt_id = t_galeriemodeletypetest.xxx_id
JOIN t_donneedico AS tdd2
ON gar_premiere_lecture = tdd2.xxx_id
JOIN t_donneedico AS tdd3
ON gar_seconde_lecture = tdd3.xxx_id
JOIN t_galeriemodeletype
ON gtt_gmt_id = t_galeriemodeletype.xxx_id
JOIN t_donneedico AS tddtype
ON gmt_type = tddtype.xxx_id
JOIN t_donneedico AS tddtest
ON gtt_test = tddtest.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND LOWER(sch_denomination) LIKE '%vibrio%'
AND LOWER(tddtest.don_lib) LIKE '%glucuronidase%'
AND gar_resultat IS True
ORDER BY t_souche.xxx_id;