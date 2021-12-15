DROP TABLE IF EXISTS old_souches_doublees;
DROP TABLE IF EXISTS old_ids_doubles;

SELECT sch_identifiant, split_part(sch_references_equi, ';', 1) AS ref_equi
INTO TEMPORARY TABLE old_souches_doublees
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi SIMILAR TO '%CIP 2[0-9]{5}%';

SELECT sch1.xxx_id AS new_id, sch2.xxx_id AS old_id 
INTO TEMPORARY TABLE old_ids_doubles
FROM t_souche AS sch1, t_souche AS sch2
WHERE (sch1.sch_identifiant, sch2.sch_identifiant) 
IN (SELECT sch_identifiant, ref_equi FROM old_souches_doublees);

UPDATE t_souche
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE sch_identifiant IN (SELECT ref_equi FROM old_souches_doublees);

DROP TABLE IF EXISTS old_souches_doublees;
DROP TABLE IF EXISTS old_ids_doubles;
