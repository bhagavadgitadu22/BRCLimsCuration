DROP TABLE IF EXISTS historiques_bacillus;

SELECT xxx_id, sch_historique, 
regexp_replace(sch_historique, E'[\\n\\r\\f\\u000B\\u0085\\u2028\\u2029;]+', ';;;', 'g') AS regex_historique
INTO TABLE historiques_bacillus
FROM t_souche
WHERE sch_historique != ''
AND LOWER(sch_denomination) LIKE '%bacillus%';
