DROP TABLE IF EXISTS strains_ok;
DROP TABLE IF EXISTS rows_ok;

SELECT row_number
INTO rows_ok
FROM all_strains
WHERE (true_strain NOT LIKE '% %'
OR (true_strain NOT SIMILAR TO '%[A-Z][a-z]%'
	AND true_strain NOT SIMILAR TO '%(, |=|:|«)%')
OR true_strain SIMILAR TO '[a-zA-Z,.]+? ?[a-zA-Z]{0,2} ?[\/.IVX0-9-]+? ?[a-zA-Z]? ?(\([0-9]{4})\)?')
AND true_strain != '';

SELECT *
INTO strains_ok
FROM all_strains
WHERE row_number IN (SELECT row_number FROM rows_ok);

DELETE FROM all_strains
WHERE row_number IN (SELECT row_number FROM rows_ok);

DROP TABLE IF EXISTS rows_ok;
