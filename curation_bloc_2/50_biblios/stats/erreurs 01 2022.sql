
--WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
--AND array_length(string_to_array(sch_bibliographie, ', '), 1) != 5
--OR sch_bibliographie SIMILAR TO '%(doi|DOI)%';

SELECT xxx_id, sch_identifiant, sch_bibliographie, regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g')
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO E'%0.1186/s12864-017-3925-x%';

SELECT xxx_id, sch_bibliographie, unnest(string_to_array(regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g'), '|')) 
FROM t_souche
ORDER BY xxx_id;

SELECT t.xxx_id, t.sch_bibliographie, a.elem, string_to_array(a.elem, ', '), a.nr
FROM t_souche AS t
LEFT JOIN LATERAL unnest(string_to_array(regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g'), '|'))
                    WITH ORDINALITY AS a(elem, nr) ON TRUE
WHERE array_length(string_to_array(a.elem, ', '), 1) != 5
AND LOWER(a.elem) SIMILAR TO '%(doi|pmid)%';

SELECT a.elem, string_to_array(a.elem, ', ')
FROM t_souche AS t
LEFT JOIN LATERAL unnest(string_to_array(regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g'), '|'))
                    WITH ORDINALITY AS a(elem, nr) ON TRUE
WHERE array_length(string_to_array(a.elem, ', '), 1) != 5
GROUP BY a.elem, string_to_array(a.elem, ', ')
ORDER BY a.elem;

SELECT a.elem, string_to_array(a.elem, ', ')
FROM t_souche AS t
LEFT JOIN LATERAL unnest(string_to_array(regexp_replace(sch_bibliographie, E';[\\n\\r]+', '|', 'g'), '|'))
                    WITH ORDINALITY AS a(elem, nr) ON TRUE
WHERE array_length(string_to_array(a.elem, ', '), 1) != 5
AND LOWER(a.elem) SIMILAR TO '%pmid%'
GROUP BY a.elem, string_to_array(a.elem, ', ')
ORDER BY a.elem;
