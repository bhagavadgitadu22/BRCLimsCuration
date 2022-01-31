/*
SELECT t_donneedico.xxx_id, don_lib, ARRAY_AGG(sch_identifiant), ARRAY_AGG(t_souche.xxx_id)
FROM t_donneedico
LEFT JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE don_dic_id = 3758
AND t_donneedico.xxx_sup_dat IS NULL
GROUP BY t_donneedico.xxx_id, don_lib
ORDER BY don_lib;
*/

UPDATE t_souche
SET sch_lieu = NULL,
	sch_dat_prelevement = TO_TIMESTAMP('1961', 'YYYY')
WHERE xxx_id = 136454;

UPDATE t_souche
SET sch_lieu = NULL,
	sch_dat_prelevement = TO_TIMESTAMP('1964', 'YYYY')
WHERE xxx_id = 531528;

UPDATE t_donneedico 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE t_donneedico.xxx_id IN (136453, 531526);
