DROP TABLE IF EXISTS valid_seven;

-- on casse les 8 éléments quand ça donne un bon 4 éléments
-- ça récupère 58 éléments de biblio
SELECT id, xxx_id, n_ligne, journal, annee, volume, first_page, last_page 
INTO TEMPORARY TABLE valid_seven
FROM

(SELECT id, xxx_id, n_ligne, 
full_trim(t.journal) AS journal,
full_trim(t.annee) AS annee,
full_trim(t.volume) AS volume,
full_trim((regexp_split_to_array(t.pages, '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(t.pages, '-|–| and '))[2]) AS last_page
FROM 
 
(SELECT id, xxx_id, n_ligne, 
doc[1] AS c1, doc[2] AS c2, doc[3] AS c3, (REGEXP_MATCHES(full_trim(doc[4]), '^([0-9]+(-|–| and )[0-9]+|[0-9]+).*'))[1] AS c4, 
(REGEXP_MATCHES(full_trim(doc[4]), '^([0-9]+(-|–| and )[0-9]+|[0-9]+)(.*)'))[3] AS c5, doc[5] AS c6, doc[6] AS c7, doc[7] AS c8 FROM

(SELECT id, xxx_id, n_ligne, doc 
FROM all_documents
WHERE array_length(doc, 1) = 7
) AS seven_elements) AS de_7_a_8

CROSS JOIN LATERAL(VALUES (c1, c2, c3, c4), (c5, c6, c7, c8)) as t(journal, annee, volume, pages)
) AS after_cut
	 
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND first_page SIMILAR TO '[0-9]+'
AND (last_page SIMILAR TO '[0-9]+[^0-9]*' OR last_page IS NULL);

-- on ajoute les lignes regroupées dans la tables des bonnes biblios dont on va chercher les dois
-- 9975 lignes après regroupement
INSERT INTO good_documents(journal, annee, volume, first_page, last_page, xxx_id, n_ligne)
SELECT DISTINCT journal, annee, volume, first_page, last_page, xxx_id, n_ligne
FROM valid_seven;

-- puis on supprime les documents gérés de all_documents
DELETE FROM all_documents
WHERE id IN (SELECT id FROM valid_seven);

DROP TABLE IF EXISTS valid_seven;
