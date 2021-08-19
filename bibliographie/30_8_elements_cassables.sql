DROP TABLE IF EXISTS valid_eight;

-- on casse les 8 éléments quand ça donne un bon 4 éléments
-- ça récupère 58 éléments de biblio
SELECT id, sch_identifiant, journal, annee, volume, first_page, last_page 
INTO TEMPORARY TABLE valid_eight
FROM

(SELECT id, sch_identifiant,
full_trim(t.journal) AS journal,
full_trim(t.annee) AS annee,
full_trim(t.volume) AS volume,
full_trim((regexp_split_to_array(t.pages, '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(t.pages, '-|–| and '))[2]) AS last_page
FROM 

(SELECT id, sch_identifiant, doc 
FROM all_documents
WHERE array_length(doc, 1) = 8
) AS eight_elements

CROSS JOIN LATERAL(VALUES (doc[1], doc[2], doc[3], doc[4]), (doc[5], doc[6], doc[7], doc[8])) as t(journal, annee, volume, pages)
) AS after_cut
	 
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO '[0-9]+'
AND (last_page SIMILAR TO '[0-9]+[^0-9]*' OR last_page IS NULL);


-- on ajoute les lignes regroupées dans la tables des bonnes biblios dont on va chercher les dois
-- 9975 lignes après regroupement
INSERT INTO good_documents(journal, annee, volume, first_page, last_page, sch_identifiant)
SELECT journal, annee, volume, first_page, last_page, sch_identifiant
FROM valid_eight;

-- puis on supprime les documents gérés de all_documents
DELETE FROM all_documents
WHERE id IN (SELECT id FROM valid_eight);

DROP TABLE IF EXISTS valid_eight;
