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
FROM (SELECT ROW_NUMBER() OVER() AS row, split_part(name_taxo, ' ', 3) AS subspecies, 
	tdd_species.don_code AS don_parent
	FROM new_elmts_dicos
	JOIN t_donneedico AS tdd_species
	ON tdd_species.don_lib = split_part(name_taxo, ' ', 2)
	AND tdd_species.don_dic_id = 3755
	AND tdd_species.xxx_sup_dat IS NULL
	JOIN t_donneedico AS tdd_genus
	ON tdd_genus.don_code = tdd_species.don_parent
	AND tdd_genus.don_lib = split_part(name_taxo, ' ', 1)
	AND tdd_genus.don_dic_id = 3755
	AND tdd_genus.xxx_sup_dat IS NULL
	WHERE type_taxo = 'subspecies') AS a;
