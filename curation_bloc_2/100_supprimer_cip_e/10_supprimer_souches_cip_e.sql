DROP TABLE IF EXISTS ids_a_supprimer;

SELECT xxx_id 
INTO TEMPORARY TABLE ids_a_supprimer
FROM t_souche 
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND LOWER(sch_identifiant) LIKE 'cip e%';

UPDATE t_souche 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (SELECT xxx_id FROM ids_a_supprimer);

DROP TABLE IF EXISTS ids_a_supprimer;
