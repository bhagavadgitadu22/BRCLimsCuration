SELECT full_trim(doc), 
ascii(left(doc, 1)) AS doc2
FROM
(SELECT trim(unnest(string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', ' ', 'g'), ';'))) AS doc
FROM t_souche) AS biblio
WHERE doc != ''
AND doc SIMILAR TO '%[a-zA-Z]+%'
GROUP BY doc;