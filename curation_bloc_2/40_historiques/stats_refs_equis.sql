UPDATE t_souche
SET sch_references_equi = btrim(sch_references_equi, ' ;')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi != btrim(sch_references_equi, ' ;');

UPDATE t_souche
SET sch_references_equi = REGEXP_REPLACE(sch_references_equi, ' ?; ?', ';', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi != REGEXP_REPLACE(sch_references_equi, ' ?; ?', ';', 'g');

UPDATE t_souche
SET sch_references_equi = REGEXP_REPLACE(sch_references_equi, E'[\\n\\r]+', '', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi != REGEXP_REPLACE(sch_references_equi, E'[\\n\\r]+', '', 'g');

UPDATE t_souche
SET sch_references_equi = REGEXP_REPLACE(sch_references_equi, ';= ', ';', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi != REGEXP_REPLACE(sch_references_equi, ';= ', ';', 'g');

SELECT sch_references_equi,
ascii(left(sch_references_equi, 1))
FROM t_souche 
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi NOT SIMILAR TO '([A-Z]+ ?[0-9.-]+;)*[A-Z]+ ?[0-9.-]+'
GROUP BY sch_references_equi;

SELECT sch_references_equi
FROM t_souche 
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_references_equi SIMILAR TO '%[^0-9a-zA-Z. -;_Δ]+%'
GROUP BY sch_references_equi;
