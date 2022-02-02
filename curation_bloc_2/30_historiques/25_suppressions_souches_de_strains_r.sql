/*
SELECT * 
FROM all_strains
WHERE LOWER(short_strain) = 'r';
*/

UPDATE t_souche
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
FROM all_strains
WHERE t_souche.xxx_id = all_strains.xxx_id
AND LOWER(short_strain) = 'r';
