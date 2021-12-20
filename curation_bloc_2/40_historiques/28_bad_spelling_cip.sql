DROP TABLE IF EXISTS cip_mispelled;

SELECT xxx_id, short_strain AS old_strain, 
REGEXP_REPLACE(short_strain, '(?<=[56]{1}[0-9]{1})(?=[0-9]{2})', '.') AS new_strain
INTO TEMPORARY TABLE cip_mispelled
FROM all_strains
WHERE short_strain SIMILAR TO 'CIP [56]{1}[0-9]{3}';

UPDATE t_souche
SET sch_historique = REPLACE(sch_historique, old_strain, new_strain)
FROM cip_mispelled
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_souche.xxx_id = cip_mispelled.xxx_id;

UPDATE all_strains 
SET short_strain = REGEXP_REPLACE(short_strain, '(?<=[56]{1}[0-9]{1})(?=[0-9]{2})', '.') 
WHERE short_strain SIMILAR TO 'CIP [56]{1}[0-9]{3}';
