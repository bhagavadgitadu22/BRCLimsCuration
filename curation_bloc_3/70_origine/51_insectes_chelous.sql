/*
SELECT sch_isole_a_partir_de, (SELECT xxx_id FROM nombre_animal)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(cadra|galleria|culiseta|amsacta|ostrinia|mansonia|simulium|culicidae|trichoplusia|scrobipalpa|pyrausta|platella|paramyelois|melolontha|earias|thaumetopoea|malacosoma|bombyx|culex|pectinophora|plodia|ephestia|hadena|lepidoptera|choristoneura|heliothis|homeosoma|lymantria|amyelois|lepidiota|diparopsis|pieris|heliotis|dendrolimus|anopheles|acyrthosiphon|sitotroga)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%sewage%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_animal)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(cadra|galleria|culiseta|amsacta|ostrinia|mansonia|simulium|culicidae|trichoplusia|scrobipalpa|pyrausta|platella|paramyelois|melolontha|earias|thaumetopoea|malacosoma|bombyx|culex|pectinophora|plodia|ephestia|hadena|lepidoptera|choristoneura|heliothis|homeosoma|lymantria|amyelois|lepidiota|diparopsis|pieris|heliotis|dendrolimus|anopheles|acyrthosiphon|sitotroga)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%sewage%';
