DROP TABLE IF EXISTS origines_refs_equis;
DROP TABLE IF EXISTS bilan_collections;

SELECT unnest(string_to_array(sch_references_equi, ';')) AS ref_equi,
split_part(unnest(string_to_array(sch_references_equi, ';')), ' ', 1) AS collection, 
split_part(unnest(string_to_array(sch_references_equi, ';')), ' ', 2) AS number
INTO origines_refs_equis
FROM t_souche;

SELECT collection, ARRAY_AGG(ref_equi), COUNT(*)
INTO bilan_collections
FROM origines_refs_equis
WHERE collection SIMILAR TO '[A-Z]+'
AND length(collection) > 1
GROUP BY collection;
