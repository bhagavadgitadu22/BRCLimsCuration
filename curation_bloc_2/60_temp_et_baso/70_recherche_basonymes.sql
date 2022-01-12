DROP TABLE IF EXISTS basonymes_a_faire;

SELECT sch.sch_identifiant, type_sch.sch_identifiant,
sch.basonyme, type_sch.basonyme,
denom
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.basonyme != type_sch.basonyme;

SELECT sch.xxx_id AS id, type_sch.xxx_id AS type_id, 
sch.sch_identifiant AS iden, type_sch.sch_identifiant AS type_iden,
sch.basonyme AS baso, type_sch.basonyme AS type_baso,
denom
INTO basonymes_a_faire
FROM last_version_souches_cip AS sch
JOIN souches_types_de_souches_short
ON id = sch.sch_identifiant
JOIN last_version_souches_cip AS type_sch
ON id_type = type_sch.sch_identifiant
WHERE sch.basonyme IS NULL AND type_sch.basonyme IS NOT NULL;

UPDATE t_string_val
SET svl_valeur = type_baso
FROM basonymes_a_faire
WHERE svl_entite_id = id;

--a priori pas besoin de INSERT si tous les éléments existent déjà dans t_string_val
--INSERT INTO t_string_val (svl_entite_id, svl_att_id, svl_valeur)
SELECT id, 2756, type_baso
FROM basonymes_a_faire
WHERE id NOT IN (SELECT svl_entite_id FROM t_string_val);
