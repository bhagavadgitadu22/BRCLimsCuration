DROP TABLE IF EXISTS valid_five;

-- on sélectionne les 4 éléments valides
-- on veut journal = texte, année en 4 chiffres et pages valides
-- 33408 lignes
SELECT id, xxx_id, n_ligne, journal, annee, volume, first_page, last_page
INTO TEMPORARY TABLE valid_five
FROM

(SELECT id, xxx_id, n_ligne, 
full_trim(CONCAT(doc[1], ',', doc[2])) AS journal,
full_trim(doc[3]) AS annee,
full_trim(doc[4]) AS volume,
full_trim((regexp_split_to_array(doc[5], '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(doc[5], '-|–| and '))[2]) AS last_page
FROM 

(SELECT id, xxx_id, n_ligne, doc 
FROM all_documents
WHERE array_length(doc, 1) = 5
) AS five_elements

) AS after_cut
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO '[0-9]+'
AND (last_page SIMILAR TO '[0-9]+[^0-9]*' OR last_page IS NULL);

-- on ajoute les lignes regroupées dans la tables des bonnes biblios dont on va chercher les dois
-- 9975 lignes après regroupement
INSERT INTO good_documents(journal, annee, volume, first_page, last_page, xxx_id, n_ligne)
SELECT DISTINCT journal, annee, volume, first_page, last_page, xxx_id, n_ligne
FROM valid_five;

-- puis on supprime les documents gérés de all_documents
DELETE FROM all_documents
WHERE id IN (SELECT id FROM valid_five);

DROP TABLE IF EXISTS valid_five;
