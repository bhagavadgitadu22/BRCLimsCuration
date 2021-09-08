DROP TABLE IF EXISTS lines_bacillus;

SELECT xxx_id, numero, line, max(annee::integer) AS bonne_annee, full_trim((regexp_matches(line, CONCAT(max(annee::integer), '(.*)'), 'g'))[1]) AS texte
INTO lines_bacillus FROM 

(SELECT xxx_id, numero, line, (regexp_matches(line, '[0-9]{4}', 'g'))[1] AS annee FROM

(SELECT hb.xxx_id, a.nr AS numero,
full_trim(regexp_replace(a.elem, 'strain .*', ';;;', 'g')) AS line
FROM historiques_bacillus hb
LEFT JOIN LATERAL unnest(string_to_array(hb.regex_historique, ';;;')) WITH ORDINALITY AS a(elem, nr) ON TRUE) AS a

WHERE line != '') AS b

GROUP BY xxx_id, numero, line;
