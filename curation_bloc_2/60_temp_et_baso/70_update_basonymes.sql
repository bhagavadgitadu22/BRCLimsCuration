DROP TABLE IF EXISTS basonymes_a_faire;

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
WHERE (sch.basonyme IS NULL AND type_sch.basonyme IS NOT NULL)
OR (sch.basonyme IS NOT NULL AND sch.basonyme != type_sch.basonyme AND type_sch.basonyme LIKE CONCAT('%', sch.basonyme, '%'));

UPDATE t_string_val
SET svl_valeur = type_baso
FROM basonymes_a_faire
WHERE svl_entite_id = id
AND svl_att_id IN (SELECT xxx_id FROM ids_champs_basonymes);

UPDATE t_string_val
SET svl_valeur = 'Beneckea natriegens'
FROM basonymes_a_faire
WHERE svl_valeur = 'Beneckea netriegens'
AND svl_att_id IN (SELECT xxx_id FROM ids_champs_basonymes);
