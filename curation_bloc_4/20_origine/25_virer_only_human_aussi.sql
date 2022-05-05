DROP TABLE IF EXISTS only_human;

SELECT last_version_souches_cip.xxx_id, don_lib, sch_isole_a_partir_de, REPLACE(sch_isole_a_partir_de, 'Human', '') AS new_isole
INTO only_human
FROM last_version_souches_cip
LEFT JOIN t_donneedico 
ON sch_origine = t_donneedico.xxx_id
WHERE sch_isole_a_partir_de = 'Human'
AND don_lib = 'Human';

UPDATE t_souche
SET sch_isole_a_partir_de = ''
FROM only_human
WHERE t_souche.xxx_id = only_human.xxx_id;
