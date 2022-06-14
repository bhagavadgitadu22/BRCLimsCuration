DROP TABLE IF EXISTS new_infos_genomes;

SELECT t_souche.xxx_id, p2m, date
INTO new_infos_genomes
FROM infos_p2m
JOIN t_souche
ON identifiant = TRIM(REGEXP_REPLACE(REPLACE(t_souche.sch_identifiant, 'T', ''), '(CIP|CRBIP) ?', ''))
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip);
