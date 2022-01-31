SELECT sch_identifiant, sch_denomination, don_lib, gar_resultat
FROM last_version_souches_cip
JOIN (SELECT gal_sch_id, don_lib, gar_resultat 
FROM t_galerieresultat
JOIN t_galerie
ON t_galerie.xxx_id = gar_gal_id
JOIN t_galeriemodeletypetest
ON t_galeriemodeletypetest.xxx_id = gar_gtt_id
JOIN t_donneedico
ON t_donneedico.xxx_id = gtt_test
WHERE don_lib = 'Beta glucuronidase') AS res
ON last_version_souches_cip.xxx_id = res.gal_sch_id
WHERE sch_denomination LIKE '%Escherichia%'
AND sch_denomination LIKE '%coli%'
ORDER BY gar_resultat DESC, sch_identifiant;
