INSERT INTO bad_strains
SELECT *
FROM all_strains
WHERE short_strain SIMILAR TO '%, %'
OR short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%'
OR short_strain SIMILAR TO '[A-Z]{1}[a-z]+ [a-z]+( «HD [0-9]+»)?'
OR LOWER(short_strain) LIKE '%v.vincent%';

DELETE
FROM all_strains
WHERE short_strain SIMILAR TO '%, %'
OR short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%'
OR short_strain SIMILAR TO '[A-Z]{1}[a-z]+ [a-z]+( «HD [0-9]+»)?'
OR LOWER(short_strain) LIKE '%v.vincent%';
