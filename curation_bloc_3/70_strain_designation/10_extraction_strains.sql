DROP TABLE IF EXISTS all_strains;

-- sélection générale des strains des historiques
SELECT *, row_number() over(PARTITION BY sch_historique) AS number_row
INTO all_strains
FROM (SELECT xxx_id, sch_historique, 
(regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1] AS strain, 
btrim(regexp_replace((regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1], 'strain', ''), ' :') AS short_strain
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)) AS t_strains
ORDER BY xxx_id;
