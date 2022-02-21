/*
SELECT sch_isole_a_partir_de, (SELECT category FROM nombre_animal)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '(duck|dog|horse|rat|pig|sheep|possum|rabbit|termite|cow|mosquito|mouse|fish|pigeon|chinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bull|bandicoot|guinea|stork|bovine|ovine|celebese|abalone|ox|slug|calf|lizard|monkey|ewe|rodent|foal|hamster|porcine|kangaroo|equine|toad)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(milk|product|manure|sediment|sauce| can|plant|catheter|corn|oxic|rearing|hook|tank)%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '(duck|dog|horse|rat|pig|sheep|possum|rabbit|termite|cow|mosquito|mouse|fish|pigeon|chinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bull|bandicoot|guinea|stork|bovine|ovine|celebese|abalone|ox|slug|calf|lizard|monkey|ewe|rodent|foal|hamster|porcine|kangaroo|equine|toad)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(milk|product|manure|sediment|sauce| can|plant|catheter|corn|oxic|rearing|hook|tank)%';
