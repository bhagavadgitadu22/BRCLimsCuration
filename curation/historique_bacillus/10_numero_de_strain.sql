DROP TABLE IF EXISTS strains_bacillus;

SELECT xxx_id, (regexp_matches(regex_historique, 'strain .*'))[1] AS strain
INTO strains_bacillus
FROM historiques_bacillus;
