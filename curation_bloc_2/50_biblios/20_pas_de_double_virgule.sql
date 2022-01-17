UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, ',,', ',')
WHERE sch_bibliographie SIMILAR TO '%,,%';
