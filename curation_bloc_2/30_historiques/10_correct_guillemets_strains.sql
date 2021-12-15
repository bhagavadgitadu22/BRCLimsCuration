DROP TABLE IF EXISTS strains_bacillus;
DROP TABLE IF EXISTS new_strains_bacillus;

SELECT xxx_id, sch_historique, (regexp_matches(sch_historique, 'strain .*'))[1] AS strain
INTO strains_bacillus
FROM t_souche;

SELECT xxx_id, sch_historique, strain,
(regexp_matches(strain, CONCAT('.*?', CHR(171))))[1] AS beginning_strain,
(regexp_matches(strain, CONCAT(CHR(171), '.*?', CHR(187))))[1] AS ending_strain
INTO new_strains_bacillus
FROM strains_bacillus
WHERE strain SIMILAR TO CONCAT('%', CHR(171), '(WHO|ATCC|DSM|NCIB|NCTC|CIP|NRRL|CN)%');

/*
SELECT xxx_id, sch_historique, regexp_replace(sch_historique, strain, CONCAT(
	btrim(beginning_strain, CONCAT(' ', CHR(171))), 
	' = ', 
	replace(btrim(ending_strain, CONCAT(CHR(171), CHR(187))), ', ', ' = ')))
FROM new_strains_bacillus;
*/

UPDATE t_souche
SET sch_historique = regexp_replace(t_souche.sch_historique, strain, CONCAT(
	btrim(beginning_strain, CONCAT(' ', CHR(171))), 
	' = ', 
	replace(btrim(ending_strain, CONCAT(CHR(171), CHR(187))), ', ', ' = ')))
FROM new_strains_bacillus
WHERE t_souche.xxx_id = new_strains_bacillus.xxx_id;
