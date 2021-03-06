DROP TABLE IF EXISTS bad_strains;
DROP TABLE IF EXISTS good_strains;

SELECT *
INTO TABLE bad_strains
FROM all_strains
WHERE short_strain SIMILAR TO '%, %';

DELETE
FROM all_strains
WHERE short_strain SIMILAR TO '%, %';

INSERT INTO bad_strains
SELECT *
FROM all_strains
WHERE short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%';

DELETE
FROM all_strains
WHERE short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%';

-- les bonnes strains
SELECT xxx_id, sch_historique, short_strain
INTO TABLE good_strains
FROM all_strains
WHERE short_strain SIMILAR TO '[-./a-zA-Z0-9]+'
OR short_strain SIMILAR TO '[A-Za-z]+ [0-9_./-]+[A-Za-z]?'
OR short_strain SIMILAR TO '[0-9]+ [A-Za-z]+'
OR short_strain SIMILAR TO '%Δ%';

DELETE FROM all_strains
WHERE short_strain SIMILAR TO '[-./a-zA-Z0-9]+'
OR short_strain SIMILAR TO '[A-Za-z]+ [0-9_./-]+[A-Za-z]?'
OR short_strain SIMILAR TO '[0-9]+ [A-Za-z]+'
OR short_strain SIMILAR TO '%Δ%';
