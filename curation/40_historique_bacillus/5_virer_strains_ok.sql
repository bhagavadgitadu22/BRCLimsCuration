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

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+', '', 'g')
FROM historiques_bacillus
WHERE t_souche.xxx_id = historiques_bacillus.xxx_id									
AND t_souche.sch_historique LIKE '%M. Piéchaud%';

UPDATE t_souche
SET sch_historique = regexp_replace(sch_historique, E'[\\n\\r ]+$', '', 'g')
WHERE sch_historique != regexp_replace(sch_historique, E'[\\n\\r ]+$', '', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E', ?[\\n\\r]+Flavobacterium meningosepticum', ', Flavobacterium meningosepticum', 'g')
WHERE sch_historique != regexp_replace(t_souche.sch_historique, E', ?[\\n\\r]+Flavobacterium meningosepticum', ', Flavobacterium meningosepticum', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'[\\n\\r]+R', 'R', 'g')
WHERE sch_historique != regexp_replace(t_souche.sch_historique, E'[\\n\\r]+R', 'R', 'g')
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'Giessen, [\\n\\r]+Germany', 'Giessen, Germany', 'g')
WHERE t_souche.xxx_id = 7311690;

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'Pyt[\\n\\r]+Akkermansia', 'Pyt, Akkermansia', 'g')
WHERE t_souche.xxx_id = 4599541;

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'EDL933[\\n\\r]+A. O''Brien', 'EDL933, A. O''Brien', 'g')
WHERE t_souche.xxx_id = 553590;

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'R711,[\\n\\r]+"Flavobacterium sp."', 'R711, Flavobacterium sp.', 'g')
WHERE t_souche.xxx_id = 154378;

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, E'France:[\\n\\r]+strain  Piyasena', 'France: strain Piyasena', 'g')
WHERE t_souche.xxx_id = 532688;
