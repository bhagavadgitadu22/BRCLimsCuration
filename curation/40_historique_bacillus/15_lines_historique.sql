-- on recupère le reste de l'historique (les années et les gens)
DROP TABLE IF EXISTS lines_bacillus;

SELECT xxx_id, numero, line, max(annee::integer) AS bonne_annee, full_trim((regexp_matches(line, CONCAT(max(annee::integer), '(.*)'), 'g'))[1]) AS texte
FROM 

(SELECT xxx_id, numero, line, (regexp_matches(line, '[0-9]{4}', 'g'))[1] AS annee FROM

(SELECT xxx_id, line, ROW_NUMBER() OVER() AS numero
FROM
(SELECT hb.xxx_id, 
full_trim(regexp_replace(unnest(string_to_array(hb.regex_historique, ';;;')), 'strain .*', ';;;', 'g')) AS line
FROM historiques_bacillus hb) AS because_of_old_postgresql) AS a

WHERE line != '') AS b

GROUP BY xxx_id, numero, line;
