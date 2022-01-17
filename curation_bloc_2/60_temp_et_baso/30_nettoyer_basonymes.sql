UPDATE t_string_val
SET svl_valeur = btrim(svl_valeur, ' "''')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur != btrim(svl_valeur, ' "''');

UPDATE t_string_val
SET svl_valeur = REGEXP_REPLACE(svl_valeur, ' ?; ?', ', ', 'g')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur != REGEXP_REPLACE(svl_valeur, ' ?; ?', ',', 'g');

UPDATE t_string_val
SET svl_valeur = REGEXP_REPLACE(svl_valeur, ' [ ]+', ' ', 'g')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur != REGEXP_REPLACE(svl_valeur, ' [ ]+', ' ', 'g');

UPDATE t_string_val
SET svl_valeur = REGEXP_REPLACE(svl_valeur, 'bacillus', 'Bacillus')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur SIMILAR TO 'bacillus%';

UPDATE t_string_val
SET svl_valeur = REGEXP_REPLACE(svl_valeur, ' ?, ?', ', ', 'g')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur SIMILAR TO '%[a-z]+,[A-Z]+%';

UPDATE t_string_val
SET svl_valeur = REPLACE(svl_valeur, 'subsp.a', 'subsp. a')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur != REPLACE(svl_valeur, 'subsp.a', 'subsp. a');

UPDATE t_string_val
SET svl_valeur = REPLACE(svl_valeur, 'subsp.b', 'subsp. b')
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur != REPLACE(svl_valeur, 'subsp.b', 'subsp. b');

/*
SELECT sch_identifiant, sch_denomination, svl_valeur
FROM t_string_val
JOIN last_version_souches_cip
ON svl_entite_id = last_version_souches_cip.xxx_id
WHERE svl_att_id = 2756
AND svl_valeur != ''
AND svl_valeur NOT SIMILAR TO '[A-Z]{1}[a-z]+ [a-z]+( [a-z]+.?)*(, [A-Z]{1}[a-z]+ [a-z]+([ ]+[a-z]+.?)*)*'
ORDER BY sch_identifiant;
*/
