/*
SELECT sch_isole_a_partir_de
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '(duck|dog|horse|rat|pig|sheep|opossum|rabbit|termite|cow|moustique|mosquito|opossum|mouton|mouse|fish|pigeon|chinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bullchinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bull)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(milk|product|manure|sediment|sauce| can|plant|catheter|cattle)%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '(duck|dog|horse|rat|pig|sheep|opossum|rabbit|termite|cow|moustique|mosquito|opossum|mouton|mouse|fish|pigeon|chinchilla|snail|hedgehog|goat|cat|frog|cockroach|oyster|bull)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(milk|product|manure|sediment|sauce| can|plant|catheter|cattle)%';

/*
SELECT sch_isole_a_partir_de
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(cadra|galleria|culiseta|amsacta|ostrinia|mansonia|simulium|culicidae|trichoplusia|scrobipalpa|pyrausta|platella|paramyelois|melolontha|earias|thaumetopoea|malacosoma|bombyx|culex|pectinophora|plodia|ephestia|hadena|lepidoptera)%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(cadra|galleria|culiseta|amsacta|ostrinia|mansonia|simulium|culicidae|trichoplusia|scrobipalpa|pyrausta|platella|paramyelois|melolontha|earias|thaumetopoea|malacosoma|bombyx|culex|pectinophora|plodia|ephestia|hadena|lepidoptera)%';

/*
SELECT sch_isole_a_partir_de
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(larva?e|chenille)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%terre%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(larva?e|chenille)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%terre%';
