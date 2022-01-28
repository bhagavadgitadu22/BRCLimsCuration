DROP TABLE IF EXISTS dois_a_corriger;
DROP TABLE IF EXISTS pmids_a_corriger;

SELECT t.xxx_id, a.nr, 
btrim((REGEXP_MATCHES(
	btrim(split_part(split_part((regexp_matches(LOWER(a.elem), 'doi.*'))[1], '. ', 1), ', ', 1), ').'), 
	'(?<=doi.org/|doi[: ]+).*'))[1], ' :') AS doi
INTO dois_a_corriger
FROM t_souche AS t
LEFT JOIN LATERAL unnest(string_to_array(regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g'), '|'))
                    WITH ORDINALITY AS a(elem, nr) ON TRUE
WHERE t.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND array_length(string_to_array(a.elem, ','), 1) != 5
AND LOWER(a.elem) SIMILAR TO '%doi%'
ORDER BY a.elem;

SELECT t.xxx_id, a.nr,
(regexp_matches(LOWER(elem), '(?<=pmid[: ]+).*'))[1] AS pmid
INTO pmids_a_corriger
FROM t_souche AS t
LEFT JOIN LATERAL unnest(string_to_array(regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g'), '|'))
                    WITH ORDINALITY AS a(elem, nr) ON TRUE
WHERE t.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t.xxx_id NOT IN (SELECT xxx_id FROM dois_a_corriger)
AND array_length(string_to_array(a.elem, ','), 1) != 5
AND LOWER(a.elem) SIMILAR TO '%pmid%'
ORDER BY a.elem;
