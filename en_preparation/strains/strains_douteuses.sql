DROP TABLE IF EXISTS strains_douteuses;

SELECT *
INTO strains_douteuses
FROM all_strains
WHERE true_strain LIKE '%, %'
OR true_strain LIKE '% %'
OR true_strain = '';
