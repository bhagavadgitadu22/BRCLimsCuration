UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, ',,', ',')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%,,%';
