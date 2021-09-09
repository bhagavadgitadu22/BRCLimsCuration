SELECT array_length(doc, 1),
doc,
array_agg(sch_identifiant)
FROM 

(SELECT sch_identifiant, doc FROM
(SELECT sch_identifiant,
 string_to_array(trim(unnest(string_to_array(regexp_replace(sch_bibliographie, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029]+', ' ', 'g'), ';'))), ',') AS doc
FROM t_souche) AS a
WHERE array_length(doc, 1) != 4) AS candidates

GROUP BY doc
ORDER BY array_length(doc, 1) DESC;