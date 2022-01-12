DROP TABLE IF EXISTS souches_types_de_souches;
DROP TABLE IF EXISTS duos_de_souches_types;
DROP TABLE IF EXISTS souches_types_de_souches_short;

SELECT sch.sch_identifiant AS id, sch_type.sch_identifiant AS id_type, 
sch.sch_type AS type_ou_pas, sch.sch_denomination AS denom
INTO TABLE souches_types_de_souches
FROM last_version_souches_cip AS sch
LEFT JOIN last_version_souches_cip AS sch_type
ON sch.sch_denomination = sch_type.sch_denomination
WHERE sch.sch_identifiant != sch_type.sch_identifiant
AND sch_type.sch_type IS True
AND sch_type.sch_denomination NOT SIMILAR TO '%( sp.|unnamed|Doublon)%'
ORDER BY sch.sch_denomination;

SELECT id 
INTO TABLE duos_de_souches_types
FROM souches_types_de_souches
WHERE type_ou_pas IS True;

SELECT *
INTO souches_types_de_souches_short
FROM souches_types_de_souches
WHERE id NOT IN (SELECT id FROM duos_de_souches_types)
ORDER BY denom;

DROP TABLE IF EXISTS souches_types_de_souches;
DROP TABLE IF EXISTS duos_de_souches_types;
