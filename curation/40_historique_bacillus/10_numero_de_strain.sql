--  on récupère la parte strain de l'historique
DROP TABLE IF EXISTS strains_bacillus;

SELECT xxx_id, (regexp_matches(regex_historique, 'strain .*'))[1] AS strain
INTO strains_bacillus
FROM historiques_bacillus;

UPDATE strains_bacillus
SET strain = regexp_replace(strain, 'strain (?=(A [0-9]+|5[0-9]{1}.[0-9]+))', 'strain CIP ')
WHERE strain SIMILAR TO 'strain (A [0-9]+|5[0-9]{1}.[0-9]+)';

UPDATE strains_bacillus
SET strain = regexp_replace(strain, 'strain (?=(A [0-9]+|5[0-9]{1}.[0-9]+))', 'strain CIP ')
WHERE strain SIMILAR TO 'strain (A [0-9]+|5[0-9]{1}.[0-9]+) «%';

UPDATE strains_bacillus
SET strain = regexp_replace(strain, 'A[ ]+', 'A')
WHERE strain SIMILAR TO 'strain CIP A[ ]+[0-9]+';

UPDATE strains_bacillus
SET strain = regexp_replace(strain, 'A[ ]+', 'A')
WHERE strain SIMILAR TO 'strain CIP A[ ]+[0-9]+ «%';

UPDATE strains_bacillus
SET strain = CONCAT(btrim((regexp_match(strain, '.*?«'))[1], ' «'), ' = ', replace(btrim((regexp_match(strain, '«.*?»'))[1], '«»'), ', ', ' = '))
WHERE strain SIMILAR TO '%«(WHO|ATCC|DSM|NCIB|NCTC|CIP|NRRL|CN)%';
