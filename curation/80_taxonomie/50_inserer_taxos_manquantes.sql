INSERT INTO t_donneedico( 
	xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	don_code, don_pos, don_lib, don_parent, don_supprimable
)
SELECT xxx_vbloc, xxx_brc_id, xxx_cre_dat, xxx_cre_usr_id, 
	xxx_maj_dat, xxx_maj_usr_id, xxx_sup_dat, xxx_sup_usr_id, don_dic_id, 
	(SELECT MAX(don_code)+1 FROM t_donneedico), (SELECT MAX(don_pos)+10 FROM t_donneedico), 'Marinitoga', 0, don_supprimable
FROM t_donneedico 
WHERE xxx_id = 110904 
AND don_dic_id = 3755
AND xxx_sup_dat IS NULL;