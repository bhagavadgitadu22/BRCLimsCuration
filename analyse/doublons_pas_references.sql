DROP TABLE IF EXISTS refs_eclatees;

SELECT ROW_NUMBER() OVER(ORDER BY xxx_id), xxx_id, sch_identifiant, sch_version, sch_references_equi, unnest(string_to_array(sch_references_equi, ';')) AS ref, sch_autres_coll
INTO refs_eclatees
FROM last_version_souches_cip
WHERE sch_references_equi != ''
ORDER BY xxx_id;

SELECT *
FROM refs_eclatees AS t_a
JOIN refs_eclatees AS t_b
ON t_a.ref = t_b.ref
AND t_a.xxx_id != t_b.xxx_id
WHERE t_a.row_number < t_b.row_number
AND NOT(t_b.sch_references_equi LIKE CONCAT('%', REPLACE(t_a.sch_identifiant, 'T', ''), '%')
OR t_a.sch_references_equi LIKE CONCAT('%', REPLACE(t_b.sch_identifiant, 'T', ''), '%'))
AND NOT(t_b.sch_references_equi LIKE CONCAT('%', REPLACE(t_a.sch_autres_coll, 'T', ''), '%')
OR t_a.sch_references_equi LIKE CONCAT('%', REPLACE(t_b.sch_autres_coll, 'T', ''), '%'));
