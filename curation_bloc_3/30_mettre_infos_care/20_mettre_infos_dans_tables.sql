DROP TABLE IF EXISTS max_identifiant;
DROP TABLE IF EXISTS infos_completes_care;

SELECT sch_identifiant, (REGEXP_MATCHES(sch_identifiant, '1[0-9]{5}'))[1]::integer AS maxi
INTO TABLE max_identifiant
FROM t_souche 
WHERE sch_identifiant SIMILAR TO 'CIP 1[0-9]{5}T?'
ORDER BY (REGEXP_MATCHES(sch_identifiant, '1[0-9]{5}'))[1]::integer DESC LIMIT 1;

SELECT CONCAT('CIP ', (SELECT maxi FROM max_identifiant)+numero) AS sch_identifiant,
now()::timestamp AS sch_dat_reception, 
sch_denomination, sch_taxonomie, sch_proprietes, sch_origine, 
sch_pto_id, sch_isole_a_partir_de, sch_lieu, TO_TIMESTAMP(sch_dat_prelevement, 'YYYY') AS sch_dat_prelevement,
sch_bibliographie, sch_temperature_incubation, sch_historique, sch_depositaire,
8376101 AS xxx_cre_usr_id, 8376101 AS xxx_maj_usr_id, 124 AS sch_statut
INTO TABLE infos_completes_care
FROM infos_care;

INSERT INTO t_souche (sch_identifiant, sch_dat_acquisition, sch_denomination, sch_taxonomie, sch_proprietes, 
					  sch_origine, sch_pto_id, sch_isole_a_partir_de, sch_lieu, sch_dat_prelevement, 
					  sch_bibliographie, sch_temperature_incubation, sch_historique, sch_depositaire,
					  xxx_cre_usr_id, xxx_maj_usr_id, sch_statut)
SELECT * FROM infos_completes_care;
