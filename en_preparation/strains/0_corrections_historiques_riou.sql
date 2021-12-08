UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, E'[\\n\\r]+', ' <- ')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_historique LIKE '%J-Y Riou, Inst. Pasteur, Paris, France%';
