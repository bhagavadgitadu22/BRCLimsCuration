/*
SELECT sch_isole_a_partir_de
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(poussière|dust|sludge|eau|mud|sediment|sewage|sand|terre|sea|grass|vasière|spring|air|lake|boue|pool| ice)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(beaufort|culex|plankton|grass|tree|seal|disease|diseaded|horse|cucumber|research|weed|egg|polychaete|zeiraphera|dairy|larvaire|vétérinaire|lépidoptaire|processionnaire|copepod)%'
GROUP BY sch_isole_a_partir_de;
*/

UPDATE t_souche
SET sch_origine = (SELECT xxx_id FROM nombre_environnement)
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_origine IS NULL
AND LOWER(sch_isole_a_partir_de) SIMILAR TO '%(poussière|dust|sludge|eau|mud|sediment|sewage|sand|terre|sea|grass|vasière|spring|air|lake|boue|pool| ice)%'
AND LOWER(sch_isole_a_partir_de) NOT SIMILAR TO '%(beaufort|culex|plankton|grass|tree|seal|disease|diseaded|horse|cucumber|research|weed|egg|polychaete|zeiraphera|dairy|larvaire|vétérinaire|lépidoptaire|processionnaire|copepod)%';
