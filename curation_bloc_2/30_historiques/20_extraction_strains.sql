DROP TABLE IF EXISTS all_strains;

SELECT xxx_id, sch_historique, 
(regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1] AS strain, 
btrim(regexp_replace((regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1], 'strain', ''), ' :') AS short_strain
INTO all_strains
FROM t_souche
ORDER BY xxx_id;

DELETE
FROM all_strains
WHERE short_strain SIMILAR TO '%, %';

DELETE
FROM all_strains
WHERE short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%';

-- les bonnes strains


-- les mauvaises strains restantes
SELECT xxx_id, sch_historique, strain, short_strain
FROM all_strains
WHERE NOT(short_strain SIMILAR TO '[-./a-zA-Z0-9]+'
OR short_strain SIMILAR TO '[A-Za-z]+ [0-9_./-]+[A-Za-z]?'
OR short_strain SIMILAR TO '[0-9]+ [A-Za-z]+'
OR short_strain SIMILAR TO '%Δ%')
ORDER BY random();
