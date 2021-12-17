UPDATE t_souche
SET sch_historique = REPLACE(sch_historique, '< -', '<-')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%< -%';

UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, ',? <:', ':', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%<:%';

UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, ' ?<(?!-) ?', ' <- ', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%<[^-]+%';

UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, '<-(?! )', '<- ', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%<-[^ ]+%';

UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, '(?<! )<-', ' <-', 'g')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique SIMILAR TO '%[^ ]+<-%';
