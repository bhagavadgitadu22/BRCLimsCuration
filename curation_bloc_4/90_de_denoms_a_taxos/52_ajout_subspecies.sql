-- puis on ajoute les species manquants
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
	subspecies, don_parent
FROM (SELECT ROW_NUMBER() OVER() AS row, short_denom, species, 
	tdd_species.don_code AS don_parent, subspecies
	FROM new_elmts_dicos
	JOIN t_donneedico AS tdd_species
	ON tdd_species.don_lib = species
	AND don_dic_id = 3755
	AND tdd_species.xxx_sup_dat IS NULL
	WHERE subspecies != '') AS a;

