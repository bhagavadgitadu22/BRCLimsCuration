DROP TABLE IF EXISTS new_elmts_dicos;
DROP TABLE IF EXISTS new_species_dico;

UPDATE taxonomy
SET sp_epithet = ''
WHERE sp_epithet IS NULL;

UPDATE taxonomy
SET subsp_epithet = ''
WHERE subsp_epithet IS NULL;

SELECT short_denom, genus, species, subspecies, CASE
	WHEN sp_epithet = '' THEN genus_name
	WHEN subsp_epithet = '' THEN CONCAT(genus_name, ' ', sp_epithet)
	ELSE CONCAT(genus_name, ' ', sp_epithet, ' ', subsp_epithet)
END
INTO new_elmts_dicos
FROM denoms_sans_taxos
JOIN taxonomy
ON short_denom = (CASE
	WHEN sp_epithet = '' THEN genus_name
	WHEN subsp_epithet = '' THEN CONCAT(genus_name, ' ', sp_epithet)
	ELSE CONCAT(genus_name, ' ', sp_epithet, ' ', subsp_epithet)
END)
ORDER BY short_denom;

SELECT ROW_NUMBER() OVER() AS row, short_denom, genus, 
tdd_genus.xxx_id AS don_parent, species AS don_lib, tdd_species.xxx_id, subspecies
INTO new_species_dico
FROM new_elmts_dicos
JOIN t_donneedico AS tdd_genus
ON tdd_genus.don_lib = genus
JOIN t_dico AS td_genus
ON tdd_genus.don_dic_id = td_genus.xxx_id
LEFT JOIN t_donneedico AS tdd_species
ON tdd_species.don_lib = species
AND tdd_species.don_parent = tdd_genus.don_code
WHERE td_genus.dic_grp_collection = '[401]'
AND tdd_species.xxx_id IS NULL;

SELECT 
	now()::timestamp, (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 
	now()::timestamp, (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 
	(SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 3755, 
	(SELECT MAX(don_code)+row FROM t_donneedico WHERE don_dic_id = 3755), 
	(SELECT MAX(don_pos)+row*10 FROM t_donneedico WHERE don_dic_id = 3755), 
	don_lib, don_parent
FROM new_species_dico;

INSERT INTO t_donneedico( 
	xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, 
	xxx_sup_usr_id, don_dic_id, 
	don_code, don_pos, don_lib, don_parent
)
SELECT 
	now()::timestamp, (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 
	now()::timestamp, (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 
	(SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 3755, 
	(SELECT MAX(don_code)+row FROM t_donneedico WHERE don_dic_id = 3755), 
	(SELECT MAX(don_pos)+row*10 FROM t_donneedico WHERE don_dic_id = 3755), 
	don_lib, don_parent
FROM new_species_dico;
