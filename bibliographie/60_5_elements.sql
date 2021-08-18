SELECT journal, annee, volume, pages, array_agg(sch_identifiant) FROM

(SELECT full_trim(CONCAT(doc[1], ',', doc[2])) AS journal,
full_trim(doc[3]) AS annee,
full_trim(doc[4]) AS volume,
full_trim(doc[5]) AS pages,
sch_identifiant
FROM 

(SELECT sch_identifiant, doc FROM
(SELECT sch_identifiant,
 string_to_array(trim(unnest(string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', ' ', 'g'), ';'))), ',') AS doc
FROM t_souche) AS a
WHERE array_length(doc, 1) = 5) AS candidates) AS after_cut
	 
WHERE journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+'
AND pages SIMILAR TO '[0-9]+-[0-9]+|[0-9]+'

GROUP BY journal, annee, volume, pages;