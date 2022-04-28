INSERT INTO t_donneedico( 
	xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	don_code, don_pos, don_lib, don_parent, don_supprimable
)
SELECT xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	(SELECT MAX(don_code)+1 FROM t_donneedico WHERE don_dic_id = 3755), (SELECT MAX(don_pos)+10 FROM t_donneedico WHERE don_dic_id = 3755), 'svalbardensis', don_code, don_supprimable
FROM t_donneedico 
WHERE don_lib = 'Arcticibacter' 
AND don_dic_id = 3755
AND don_parent = 0
AND xxx_sup_dat IS NULL;

INSERT INTO t_donneedico( 
	now()::timestamp, (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 
	now()::timestamp, (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 
	(SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin'), 3755, 
	don_code, don_pos, don_lib, don_parent, don_supprimable
)
SELECT xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	(SELECT MAX(don_code)+1 FROM t_donneedico WHERE don_dic_id = 3755), (SELECT MAX(don_pos)+10 FROM t_donneedico WHERE don_dic_id = 3755), 'aurum', don_code, don_supprimable
FROM t_donneedico 
WHERE don_lib = 'Mycolicibacterium' 
AND don_dic_id = 3755
AND don_parent = 0
AND xxx_sup_dat IS NULL;

INSERT INTO t_donneedico( 
	xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	don_code, don_pos, don_lib, don_parent, don_supprimable
)
SELECT xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	(SELECT MAX(don_code)+1 FROM t_donneedico WHERE don_dic_id = 3755), (SELECT MAX(don_pos)+10 FROM t_donneedico WHERE don_dic_id = 3755), 'hirudinis', don_code, don_supprimable
FROM t_donneedico 
WHERE don_lib = 'Niabella' 
AND don_dic_id = 3755
AND don_parent = 0
AND xxx_sup_dat IS NULL;
