SELECT sch_bibliographie, ARRAY_AGG(sch_identifiant)
FROM t_souche
WHERE regexp_replace(sch_bibliographie, E'[\\n\\r]+', '|', 'g') NOT SIMILAR TO E'([^|;]+;[|]{1})*[^|;]+'
AND sch_bibliographie != ''
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
GROUP BY sch_bibliographie;
