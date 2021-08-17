CREATE OR REPLACE FUNCTION full_trim(elmt text) RETURNS text AS $$
	BEGIN
		RETURN btrim(REPLACE(REPLACE(elmt, CHR(13), ' '), CHR(10), ' '), ';. ');
	END;
$$ LANGUAGE plpgsql;

SELECT * FROM
(SELECT full_trim(doc[1]) AS journal,
full_trim(doc[2]) AS annee,
full_trim(doc[3]) AS volume,
full_trim(doc[4]) AS pages
FROM 
(SELECT string_to_array(trim(unnest(string_to_array(sch_bibliographie, E'[\\n\\r]+'))), ',') AS doc
FROM t_souche) AS biblio
WHERE array_length(doc, 1) = 4
GROUP BY doc) AS candidates
WHERE annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+'
AND pages SIMILAR TO '[0-9]+-[0-9]+|[0-9]+';