DROP TABLE IF EXISTS valid_three;

-- on sélectionne les 4 éléments valides
-- on veut journal = texte, année en 4 chiffres et pages valides
-- 33408 lignes
SELECT id, sch_identifiant, journal, annee, volume, first_page, last_page
INTO TEMPORARY TABLE valid_three
FROM

(SELECT id, sch_identifiant, 
full_trim(doc[1]) AS journal,
(REGEXP_MATCHES(full_trim(doc[2]), '^([0-9]{4}).*?[0-9]+$'))[1] AS annee,
(REGEXP_MATCHES(full_trim(doc[2]), '^[0-9]{4}.*?([0-9]+)$'))[1] AS volume,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(doc[3], '-|–| and '))[2]) AS last_page
FROM 

(SELECT id, sch_identifiant, doc 
FROM all_documents
WHERE array_length(doc, 1) = 3
) AS five_elements

) AS after_cut
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO '[0-9]+'
AND (last_page SIMILAR TO '[0-9]+[^0-9]*' OR last_page IS NULL);

-- on ajoute les lignes regroupées dans la tables des bonnes biblios dont on va chercher les dois
-- 9975 lignes après regroupement
INSERT INTO good_documents(journal, annee, volume, first_page, last_page, sch_identifiant)
SELECT DISTINCT journal, annee, volume, first_page, last_page, sch_identifiant
FROM valid_three;

-- puis on supprime les documents gérés de all_documents
DELETE FROM all_documents
WHERE id IN (SELECT id FROM valid_three);

DROP TABLE IF EXISTS valid_three;
