CREATE OR REPLACE FUNCTION full_trim(elmt text) RETURNS text AS $$
        BEGIN
                RETURN trim(elmt);
        END;
$$ LANGUAGE plpgsql;

SELECT * FROM
(SELECT ascii(left(trim(doc[1]), 1)) AS journal, trim(doc[1]) AS journal2,
trim(doc[2]) AS annee,
trim(doc[3]) AS volume,
trim(REGEXP_REPLACE(doc[4], '\.|;| ', '')) AS pages
FROM 
(SELECT string_to_array(trim(unnest(string_to_array(sch_bibliographie, E'\n'))), ',') AS doc
FROM t_souche) AS biblio
WHERE array_length(doc, 1) = 4
GROUP BY doc) AS candidates
WHERE annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+';