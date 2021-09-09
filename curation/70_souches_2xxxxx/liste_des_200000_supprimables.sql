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

UPDATE t_alerte_souche
SET als_sch_id = new_id
FROM old_ids_doubles
WHERE als_sch_id = old_id;

UPDATE t_cousinage
SET sch_id_principal = new_id
FROM old_ids_doubles
WHERE sch_id_principal = old_id;

UPDATE t_cousinage
SET sch_id_secondaire = new_id
FROM old_ids_doubles
WHERE sch_id_secondaire = old_id;

UPDATE t_carac_phenotypique_resultat
SET cpr_sch_id = new_id
FROM old_ids_doubles
WHERE cpr_sch_id = old_id;

UPDATE t_souche_t_carac_phenotypique_resultat
SET strainentity_xxx_id = new_id
FROM old_ids_doubles
WHERE strainentity_xxx_id = old_id;

UPDATE t_miseenculture
SET mec_sch_id = new_id
FROM old_ids_doubles
WHERE mec_sch_id = old_id
AND (new_id, mec_rang) NOT IN (SELECT mec_sch_id, mec_rang FROM t_miseenculture);

DELETE FROM t_miseenculture
WHERE mec_sch_id IN (SELECT old_id FROM old_ids_doubles);

UPDATE t_sequence
SET seq_sch_id = new_id
FROM old_ids_doubles
WHERE seq_sch_id = old_id
AND (xxx_brc_id, seq_type, new_id) NOT IN (SELECT xxx_brc_id, seq_type, seq_sch_id FROM t_sequence);

DELETE FROM t_sequence
WHERE seq_sch_id IN (SELECT old_id FROM old_ids_doubles);

DELETE FROM t_souche
WHERE sch_identifiant IN (SELECT ref_equi FROM old_souches_doublees);

DROP TABLE IF EXISTS old_souches_doublees;
DROP TABLE IF EXISTS old_ids_doubles;
