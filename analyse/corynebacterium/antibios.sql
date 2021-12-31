SELECT DISTINCT ON (sch_identifiant) 
ant_dat_realisation, t_nom.don_lib, t_res.don_lib
FROM t_souche
JOIN t_antibiogramme
ON ant_sch_id = t_souche.xxx_id
JOIN t_donneedico AS t_nom
ON ant_genre = t_nom.xxx_id
JOIN t_antibiogrammeresultat
ON anr_ant_id = t_antibiogramme.xxx_id
JOIN t_donneedico AS t_res
ON anr_resultat = t_res.xxx_id
WHERE sch_identifiant = 'CIP 100044'
ORDER BY sch_identifiant, sch_version DESC;
