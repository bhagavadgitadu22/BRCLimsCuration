-- on update les erreurs d'historique qui sont particulières
UPDATE t_souche
SET sch_historique = regexp_replace(historiques_bacillus.sch_historique, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+', '', 'g')
FROM historiques_bacillus
WHERE t_souche.xxx_id = historiques_bacillus.xxx_id
AND historiques_bacillus.sch_historique SIMILAR TO '%<-%'
AND array_length(string_to_array(regex_historique, ';;;'), 1) < 3;

UPDATE t_souche
SET sch_historique = '2020, P. Kâmpfer, Giessen Univ., Giessen, Germany: strain JJ-79'
WHERE t_souche.xxx_id = 7311772
OR t_souche.xxx_id = 7311437;

UPDATE t_souche
SET sch_historique = CONCAT('1978 ', sch_historique)
WHERE t_souche.xxx_id = 442139;

UPDATE t_souche
SET sch_historique = CONCAT('1994 ', sch_historique)
WHERE t_souche.xxx_id = 486861;
