DROP TABLE IF EXISTS valid_four;

-- on sélectionne les 4 éléments valides
-- on veut journal = texte, année en 4 chiffres et pages valides
-- 33408 lignes
SELECT id, sch_identifiant, journal, annee, volume, first_page
INTO TABLE valid_four
FROM

(SELECT id, sch_identifiant, 
full_trim(doc[1]) AS journal,
full_trim(doc[2]) AS annee,
full_trim(doc[3]) AS volume,
full_trim(doc[4]) AS first_page
FROM 

(SELECT id, sch_identifiant, doc 
FROM all_documents
WHERE array_length(doc, 1) = 4
) AS four_elements

) AS after_cut
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO 'e[-0-9]+%';

-- on ajoute les lignes regroupées dans la tables des bonnes biblios dont on va chercher les dois
-- 9975 lignes après regroupement
INSERT INTO good_documents(journal, annee, volume, first_page, last_page, sch_identifiant)
SELECT DISTINCT journal, annee, volume, first_page, NULL, sch_identifiant
FROM valid_four;

-- puis on supprime les documents gérés de all_documents
DELETE FROM all_documents
WHERE id IN (SELECT id FROM valid_four);

DROP TABLE IF EXISTS valid_four;
