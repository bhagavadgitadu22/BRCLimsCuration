UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, ' \| ', ', ', 'g')
WHERE sch_bibliographie LIKE '% | %'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'(?<=;)[ ]+(?=[\\n\\r]+)', '', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'(?<=;)[ ]+(?=[\\n\\r]+)', '', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[\\n\\r ]+$', '', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[\\n\\r ]+$', '', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E';$', '.', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E';$', '.', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[.](?=[\\n\\r]+(?!doi|[0-9]{4}))', ';', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[.](?=[\\n\\r]+(?!doi|[0-9]{4}))', ';', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[.][\\n\\r]+(?=doi|[0-9]{4})', ', ', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[.][\\n\\r]+(?=doi|[0-9]{4})', ', ', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, '; (?!DOI|[0-9]+)', E';\n', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, '; (?!DOI|[0-9]+)', E';\n', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, ';[ ]*(?=DOI|[0-9]+)', ', ', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, ';[ ]*(?=DOI|[0-9]+)', ', ', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'[;, ]*[\\n\\r]+(?=[0-9]+)(?!18th)', E', ', 'g')
WHERE sch_bibliographie != regexp_replace(sch_bibliographie, E'[;, ]*[\\n\\r]+(?=[0-9]+)(?!18th)', E', ', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

