UPDATE t_souche
SET sch_historique = REPLACE(sch_historique, CHR(127), '')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique LIKE CONCAT('%', CHR(127), '%');

UPDATE t_souche
SET sch_historique = REPLACE(sch_historique, 'strain B 8 : strain B 8', 'strain B 8')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique LIKE '%strain B 8 : strain B 8%';

UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, '[ ]+ ', ' ')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%[ ]+ %';
