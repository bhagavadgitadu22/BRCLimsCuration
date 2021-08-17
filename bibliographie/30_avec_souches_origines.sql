CREATE OR REPLACE FUNCTION full_trim(elmt text) RETURNS text AS $$
	BEGIN
		RETURN btrim(REPLACE(REPLACE(REPLACE(REPLACE(elmt, CHR(127), ' '), CHR(9), ' '), CHR(13), ' '), CHR(10), ' '), ';. ');
	END;
$$ LANGUAGE plpgsql;

SELECT journal, annee, volume, pages, array_agg(sch_identifiant) FROM

(SELECT sch_identifiant, 
full_trim(doc[1]) AS journal,
full_trim(doc[2]) AS annee,
full_trim(doc[3]) AS volume,
split_part(full_trim(doc[4]), '-', 1) AS pages
FROM 

(SELECT sch_identifiant, doc FROM
(SELECT sch_identifiant,
 string_to_array(trim(unnest(string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', ' ', 'g'), ';'))), ',') AS doc
FROM t_souche) AS a
WHERE array_length(doc, 1) = 4) AS candidates) AS after_cut

WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+'
AND pages SIMILAR TO '[0-9]+-[0-9]+|[0-9]+'

GROUP BY journal, annee, volume, pages;