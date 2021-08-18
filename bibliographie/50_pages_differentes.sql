SELECT journal, annee, volume, first_page, array_agg(sch_identifiant) FROM

(SELECT sch_identifiant, 
full_trim(doc[1]) AS journal,
full_trim(doc[2]) AS annee,
full_trim(doc[3]) AS volume,
full_trim(doc[4]) as pages,
full_trim((regexp_split_to_array(doc[4], '-|–| and '))[1]) AS first_page,
full_trim((regexp_split_to_array(doc[4], '-|–| and '))[2]) AS last_page
FROM 

(SELECT sch_identifiant, doc FROM
(SELECT sch_identifiant,
 string_to_array(trim(unnest(string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', ' ', 'g'), ';'))), ',') AS doc
FROM t_souche) AS a
WHERE array_length(doc, 1) = 4) AS candidates) AS after_cut

WHERE NOT(journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+'
AND pages SIMILAR TO '[0-9]+-[0-9]+|[0-9]+')
AND journal SIMILAR TO '%[a-zA-Z]+%'
AND annee SIMILAR TO '[0-9]{4}'
AND volume SIMILAR TO '[0-9]+'
AND first_page SIMILAR TO '[0-9]+'
AND last_page SIMILAR TO '[0-9]+[^0-9]*'

GROUP BY journal, annee, volume, first_page;