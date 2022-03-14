INSERT INTO bad_strains
SELECT *
FROM all_strains
WHERE short_strain SIMILAR TO '%, %'
OR short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%'
OR short_strain SIMILAR TO '[A-Z]{1}[a-z]+ [a-z]+( «HD [0-9]+»)?'
OR LOWER(short_strain) LIKE '%v.vincent%'
OR short_strain SIMILAR TO '%Poudre%'
OR short_strain SIMILAR TO '%derived from%'
OR short_strain SIMILAR TO '%B. tuviensis%'
OR short_strain SIMILAR TO '%vectreur clonage%'
OR LOWER(short_strain) LIKE '%serovar%'
OR short_strain LIKE '%galleriae%';

DELETE
FROM all_strains
WHERE short_strain SIMILAR TO '%, %'
OR short_strain SIMILAR TO '% [A-Z]{1}[a-z]+ [a-z]+%'
OR short_strain SIMILAR TO '[A-Z]{1}[a-z]+ [a-z]+( «HD [0-9]+»)?'
OR LOWER(short_strain) LIKE '%v.vincent%'
OR short_strain SIMILAR TO '%Poudre%'
OR short_strain SIMILAR TO '%derived from%'
OR short_strain SIMILAR TO '%B. tuviensis%'
OR short_strain SIMILAR TO '%vectreur clonage%'
OR LOWER(short_strain) LIKE '%serovar%'
OR short_strain LIKE '%galleriae%';
