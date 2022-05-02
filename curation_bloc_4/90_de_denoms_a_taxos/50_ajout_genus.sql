-- on commence par ajouter les genus manquants
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
	name_taxo, 0
FROM (SELECT ROW_NUMBER() OVER() AS row, name_taxo
	  FROM new_elmts_dicos
	  WHERE type_taxo = 'genus') AS a;
