UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, ',,', ',', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie SIMILAR TO '%,,%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'doi10.1099/isjem0.004002', 'doi: 10.1099/isjem0.004002')
WHERE xxx_id = 5466281;

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'doi: 0.1186/s12864-017-3925-x', 'doi: 10.1186/s12864-017-3925-x')
WHERE xxx_id IN (6293287, 6294270);
