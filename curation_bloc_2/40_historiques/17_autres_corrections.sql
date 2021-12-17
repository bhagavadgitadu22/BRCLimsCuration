UPDATE t_souche
SET sch_historique = REPLACE(sch_historique, CHR(127), '')
WHERE sch_historique LIKE CONCAT('%', CHR(127), '%');

UPDATE t_souche
SET sch_historique = REPLACE(sch_historique, 'strain B 8 : strain B 8', 'strain B 8')
WHERE sch_historique LIKE '%strain B 8 : strain B 8%';
