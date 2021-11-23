UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, ' \| ', ', ', 'g')
WHERE sch_bibliographie LIKE '% | %';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'(?<=;)[ ]+(?=[\\n\\r]+)', '', 'g')
WHERE sch_bibliographie SIMILAR TO E'%;([ ]+)[\\n\\r]+%';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[\\n\\r]+$', '', 'g')
WHERE sch_bibliographie SIMILAR TO E'%[\\n\\r]+';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E';$', '.', 'g')
WHERE sch_bibliographie SIMILAR TO E'%;';

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[.](?=[\\n\\r]+(?!doi|[0-9]{4}))', ';', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[.](?=[\\n\\r]+(?!doi|[0-9]{4}))', ';', 'g');

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[.][\\n\\r]+(?=doi|[0-9]{4})', ', ', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[.][\\n\\r]+(?=doi|[0-9]{4})', ', ', 'g');

SELECT sch_bibliographie, ARRAY_AGG(sch_identifiant)
FROM t_souche
WHERE regexp_replace(sch_bibliographie, E'[\\n\\r]+', '|', 'g') NOT SIMILAR TO E'([^|;]+;[|]{1})*[^|;]+'
AND sch_bibliographie != ''
GROUP BY sch_bibliographie;