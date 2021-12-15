DROP TABLE IF EXISTS valid_three;

-- on sélectionne les 4 éléments valides
-- on veut journal = texte, année en 4 chiffres et pages valides
-- 33408 lignes
SELECT id, xxx_id, n_ligne, journal, annee, volume, first_page, last_page
INTO TEMPORARY TABLE valid_three
FROM

(SELECT id, xxx_id, n_ligne, 
(REGEXP_MATCHES(doc[1], '(.*)[0-9]{4}'))[1] AS journal,
(REGEXP_MATCHES(doc[1], '.*([0-9]{4})'))[1] AS annee,
full_trim(doc[2]) AS volume,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[2]) AS last_page
FROM 

(SELECT id, xxx_id, n_ligne, doc 
FROM all_documents
WHERE array_length(doc, 1) = 3
) AS five_elements

) AS after_cut
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO '[0-9]+'
AND (last_page SIMILAR TO '[0-9]+[^0-9]*' OR last_page IS NULL);

-- on ajoute les éléments à 3 sans volume déclaré
INSERT INTO valid_three
SELECT id, xxx_id, n_ligne, journal, volume, annee, first_page, last_page
FROM

(SELECT id, xxx_id, n_ligne, 
full_trim(doc[1]) AS journal,
full_trim(doc[2]) AS annee,
NULL AS volume,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[2]) AS last_page
FROM 

(SELECT id, xxx_id, n_ligne, doc 
FROM all_documents
WHERE array_length(doc, 1) = 3
) AS five_elements

) AS after_cut
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO '[0-9]+'
AND last_page SIMILAR TO '[0-9]+[^0-9]*';

-- on ajoute les éléments sans année
INSERT INTO valid_three
SELECT id, xxx_id, n_ligne, journal, volume, annee, first_page, last_page
FROM

(SELECT id, xxx_id, n_ligne, 
full_trim(doc[1]) AS journal,
NULL AS annee,
full_trim(doc[2]) AS volume,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[2]) AS last_page
FROM 

(SELECT id, xxx_id, n_ligne, doc 
FROM all_documents
WHERE array_length(doc, 1) = 3
) AS five_elements

) AS after_cut
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND first_page SIMILAR TO '[0-9]+'
AND last_page SIMILAR TO '[0-9]+[^0-9]*';

-- on ajoute les lignes regroupées dans la tables des bonnes biblios dont on va chercher les dois
-- 9975 lignes après regroupement
INSERT INTO good_documents(journal, annee, volume, first_page, last_page, xxx_id, n_ligne)
SELECT DISTINCT journal, annee, volume, first_page, last_page, xxx_id, n_ligne
FROM valid_three;

-- puis on supprime les documents gérés de all_documents
DELETE FROM all_documents
WHERE id IN (SELECT id FROM valid_three);

DROP TABLE IF EXISTS valid_three;
