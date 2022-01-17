UPDATE t_souche
SET sch_references_equi = REPLACE(sch_references_equi, 'A359/72)', 'A359/72')
WHERE sch_references_equi LIKE '%A359/72)%';

UPDATE t_souche
SET sch_references_equi = REPLACE(sch_references_equi, 'LNP -1993)', 'LNP-1993')
WHERE sch_references_equi LIKE '%LNP -1993)%';

UPDATE t_souche
SET sch_references_equi = REPLACE(sch_references_equi, '438(3a', '438(3a)')
WHERE sch_references_equi LIKE '%438(3a%';

UPDATE t_souche
SET sch_references_equi = REPLACE(sch_references_equi, '{9834}', '9834')
WHERE sch_references_equi LIKE '%{9834}%';
