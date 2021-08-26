UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Antimicrob', 'J. Antimicrob')
WHERE sch_bibliographie LIKE '%J; Antimicrob%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Clin', 'J. Clin')
WHERE sch_bibliographie LIKE '%J; Clin%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int; J', 'Int. J')
WHERE sch_bibliographie LIKE '%Int; J%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Gen', 'J. Gen')
WHERE sch_bibliographie LIKE '%J; Gen%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Path; Microbiol', 'Acta Path. Microbiol')
WHERE sch_bibliographie LIKE '%Acta Path; Microbiol%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int. J. Syst; Evol', 'Int. J. Syst. Evol')
WHERE sch_bibliographie LIKE '%Int. J. Syst; Evol%';

UPDATE t_souche
SET sch_bibliographie = REGEXP_REPLACE(sch_bibliographie, E'Int. J. Syst. Evol. Microbiol.[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', 'Int. J. Syst. Evol. Microbiol.,')
WHERE sch_bibliographie SIMILAR TO E'%Int. J. Syst. Evol. Microbiol.[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+%';

DROP TABLE IF EXISTS nouveaux_extraits;

SELECT * 
INTO TEMPORARY TABLE nouveaux_extraits
FROM
(SELECT xxx_id, sch_bibliographie,
(REGEXP_MATCHES(sch_bibliographie, E'([\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*([^a-zA-Z]+))', 'g'))[1] AS vieil_extrait, 
btrim(full_trim((REGEXP_MATCHES(sch_bibliographie, E'([\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*([^a-zA-Z]+))', 'g'))[1]), ', ') AS bon_extrait
FROM t_souche
WHERE sch_bibliographie SIMILAR TO E'%[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*[^a-zA-Z]+') AS a
WHERE bon_extrait SIMILAR TO '%[0-9]+%';

INSERT INTO nouveaux_extraits
SELECT * 
FROM
(SELECT xxx_id, sch_bibliographie,
(REGEXP_MATCHES(sch_bibliographie, E'([\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*([^a-zA-Z]+)[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*)', 'g'))[1] AS vieil_extrait, 
btrim(full_trim((REGEXP_MATCHES(sch_bibliographie, E'([\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*([^a-zA-Z]+)[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*)', 'g'))[1]), ', ') AS bon_extrait
FROM t_souche
WHERE sch_bibliographie SIMILAR TO E'%[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*[^a-zA-Z]+[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+( [\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+)*%') AS a
WHERE bon_extrait SIMILAR TO '%[0-9]+%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(t_souche.sch_bibliographie, vieil_extrait, CONCAT(', ', bon_extrait))
FROM nouveaux_extraits
WHERE t_souche.xxx_id = nouveaux_extraits.xxx_id;
