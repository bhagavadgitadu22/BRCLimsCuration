DROP TABLE IF EXISTS liste_collections;

SELECT * 
INTO liste_collections
FROM

(SELECT (REGEXP_MATCHES(ref_equi, '[a-zA-Z]+(?= )'))[1] AS collection, ARRAY_AGG(ref_equi), COUNT(*) 
FROM

(SELECT unnest(string_to_array(sch_references_equi, ';')) as ref_equi
FROM t_souche
WHERE sch_references_equi != '') AS a

GROUP BY (REGEXP_MATCHES(ref_equi, '[a-zA-Z]+(?= )'))[1]
HAVING COUNT(*) > 2
ORDER BY COUNT(*)) AS a

WHERE char_length(collection) > 1;

SELECT xxx_id, sch_historique, strain, true_strain, first_word FROM

(SELECT xxx_id, sch_historique, strain, true_strain, 
(REGEXP_MATCHES(true_strain, '[a-zA-Z]+(?= )'))[1] AS first_word
FROM strains_douteuses) AS a

JOIN liste_collections
ON first_word = collection;
