SELECT (REGEXP_MATCHES(LOWER(sch_historique), '(hofnung|schwartz|pugsley|monod|jacob)'))[1], 
sch_catalogue, COUNT(*), ARRAY_AGG(sch_identifiant), 
ARRAY_AGG(sch_denomination), ARRAY_AGG(sch_historique)
FROM t_souche
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND LOWER(sch_historique) SIMILAR TO '%(hofnung|schwartz|pugsley|monod|jacob)%'
GROUP BY (REGEXP_MATCHES(LOWER(sch_historique), '(hofnung|schwartz|pugsley|monod|jacob)'))[1], sch_catalogue;