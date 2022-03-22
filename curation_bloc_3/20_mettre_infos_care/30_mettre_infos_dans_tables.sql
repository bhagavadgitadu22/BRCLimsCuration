DROP TABLE IF EXISTS max_identifiant;
DROP TABLE IF EXISTS max_cpt;
DROP TABLE IF EXISTS infos_completes_care;

SELECT sch_identifiant, (REGEXP_MATCHES(sch_identifiant, '1[0-9]{5}'))[1]::integer AS maxi
INTO TABLE max_identifiant
FROM t_souche 
WHERE sch_identifiant SIMILAR TO 'CIP 1[0-9]{5}T?'
ORDER BY (REGEXP_MATCHES(sch_identifiant, '1[0-9]{5}'))[1]::integer DESC LIMIT 1;

SELECT MAX(sch_cpt_id) AS maxi
INTO TABLE max_cpt
FROM t_souche;

SELECT CONCAT('CIP ', (SELECT maxi FROM max_identifiant)+numero) AS sch_identifiant, 
sch_denomination, sch_taxonomie, sch_proprietes, sch_origine, 
sch_pto_id, sch_isole_a_partir_de, sch_lieu, TO_TIMESTAMP(sch_dat_prelevement, 'YYYY') AS sch_dat_prelevement,
sch_bibliographie, sch_temperature_incubation, sch_historique, sch_depositaire,
(SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin') AS xxx_cre_usr_id,
(SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin') AS xxx_maj_usr_id, 
now()::timestamp AS sch_dat_acquisition, 124 AS sch_statut, 413 AS sch_col_id, 
1 AS xxx_brc_id, 1 AS sch_version, (SELECT maxi FROM max_cpt)+numero AS sch_cpt_id
INTO TABLE infos_completes_care
FROM infos_care;

INSERT INTO t_souche (sch_identifiant, sch_denomination, sch_taxonomie, sch_proprietes, sch_origine, 
					  sch_pto_id, sch_isole_a_partir_de, sch_lieu, sch_dat_prelevement, sch_bibliographie, 
					  sch_temperature_incubation, sch_historique, sch_depositaire, xxx_cre_usr_id, xxx_maj_usr_id,
					  sch_dat_acquisition, sch_statut, sch_col_id, xxx_brc_id, sch_version, sch_cpt_id)  
SELECT * FROM infos_completes_care;
