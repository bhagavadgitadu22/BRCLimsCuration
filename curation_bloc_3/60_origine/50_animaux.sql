/*
SELECT sch_isole_a_partir_de
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '(duck|dog|horse|rat|pig|sheep|opossum|rabbit|termite|cow|moustique|mosquito|opossum|mouton|mouse|fish|pigeon|chinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bullchinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bull|bandicoot|guinea|insect|stork|bovine|ovine|celebese|abalone)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(milk|product|manure|sediment|sauce| can|plant|catheter|corn)%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '(duck|dog|horse|rat|pig|sheep|opossum|rabbit|termite|cow|moustique|mosquito|opossum|mouton|mouse|fish|pigeon|chinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bullchinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bull|bandicoot|guinea|insect|stork|bovine|ovine|celebese|abalone)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(milk|product|manure|sediment|sauce| can|plant|catheter|corn)%';
