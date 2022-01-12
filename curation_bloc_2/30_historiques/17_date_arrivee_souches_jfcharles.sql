UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, '2009, CIP <- 2008, J.?F.? Charles', '2009, J.F. Charles')
WHERE sch_historique SIMILAR TO '2009, CIP <- 2008, J.?F.? Charles%';

UPDATE t_souche
SET sch_historique = REGEXP_REPLACE(sch_historique, '2008, J.?F.? Charles', '2009, J.F. Charles')
WHERE sch_historique SIMILAR TO '2008, J.?F.? Charles%';
