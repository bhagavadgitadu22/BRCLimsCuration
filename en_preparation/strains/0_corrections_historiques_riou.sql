UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, E'[\\n\\r]+', ' <- ')
WHERE sch_historique LIKE '%J-Y Riou, Inst. Pasteur, Paris, France%';
