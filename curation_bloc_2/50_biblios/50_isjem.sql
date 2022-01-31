/*
SELECT sch_bibliographie, REPLACE(sch_bibliographie, 'International Journal of Systematic and Evolutionary Microbiology', 'Int. J. Syst. Evol. Microbiol')
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'International Journal of Systematic and Evolutionary Microbiology', 'Int. J. Syst. Evol. Microbiol');
*/

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'International Journal of Systematic and Evolutionary Microbiology', 'Int. J. Syst. Evol. Microbiol')
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'International Journal of Systematic and Evolutionary Microbiology', 'Int. J. Syst. Evol. Microbiol');
