SELECT sch_identifiant, sch_references_equi, (REGEXP_MATCHES(sch_references_equi, '(DSM .*?)(;|$)'))[1], sch_denomination
FROM t_souche 
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_lieu IS NULL
AND sch_references_equi LIKE '%DSM%'