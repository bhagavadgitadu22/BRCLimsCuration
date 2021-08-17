CREATE OR REPLACE FUNCTION full_trim(elmt text) RETURNS text AS $$
        BEGIN
                RETURN btrim(REGEXP_REPLACE(elmt, E'\n', ''), ';. ');
        END;
$$ LANGUAGE plpgsql;

SELECT * FROM
(SELECT ascii(left(full_trim(doc[1]), 1)) AS journal, trim(doc[1]) AS journal2,
trim(doc[2]) AS annee,
trim(doc[3]) AS volume,
trim(doc[4]) AS pages,
ascii(right(full_trim(doc[4]), 1)) AS pages2
FROM 
(SELECT string_to_array(trim(unnest(string_to_array(sch_bibliographie, E'[\\n\\r]+'))), ',') AS doc
FROM t_souche) AS biblio
WHERE array_length(doc, 1) = 4
GROUP BY doc) AS candidates
WHERE annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+';