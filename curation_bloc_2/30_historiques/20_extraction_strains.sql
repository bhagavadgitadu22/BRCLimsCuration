DROP TABLE IF EXISTS all_strains;

-- sélection générale des strains des historiques
SELECT DISTINCT xxx_id, sch_historique, 
(regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1] AS strain, 
btrim(regexp_replace((regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1], 'strain', ''), ' :') AS short_strain,
row_number() over(PARTITION BY xxx_id)
INTO all_strains
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
ORDER BY xxx_id;
