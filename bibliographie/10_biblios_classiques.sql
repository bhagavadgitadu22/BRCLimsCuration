SELECT * FROM (
	
SELECT full_trim(doc[1]) AS journal,
full_trim(doc[2]) AS annee,
full_trim(doc[3]) AS volume,
split_part(full_trim(doc[4]), '-', 1) AS pages
FROM 

(SELECT string_to_array(trim(unnest(string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', ' ', 'g'), ';'))), ',') AS doc
FROM t_souche) AS biblio
) AS candidates
 
WHERE journal SIMILAR TO '%[a-zA-Z]+'
AND annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+'
AND pages SIMILAR TO '[0-9]+-[0-9]+|[0-9]+'

GROUP BY journal, annee, volume, pages;