SELECT sch_identifiant, don_lib 
FROM souches_de_champis
JOIN t_alerte_souche
ON als_sch_id = souches_de_champis.xxx_id
JOIN t_donneedico
ON als_alerte = t_donneedico.xxx_id;

SELECT sch_identifiant, don_lib AS type_sequence, seq_sequence, 
seq_blast, seq_qualite, seq_lien_base_publique, seq_com
FROM souches_de_champis
JOIN t_sequence
ON seq_sch_id = souches_de_champis.xxx_id
JOIN t_donneedico
ON seq_type = t_donneedico.xxx_id;

SELECT sch_identifiant, tdd1.don_lib AS type_galerie, 
gal_code, gal_dat_realisation, gal_com,
tdd2.don_lib AS premiere_lecture,
tdd3.don_lib AS seconde_lecture
FROM souches_de_champis
JOIN t_galerie
ON gal_sch_id = souches_de_champis.xxx_id
JOIN t_donneedico AS tdd1
ON gal_type = tdd1.xxx_id
JOIN t_galerieresultat
ON gar_gal_id = t_galerie.xxx_id
LEFT JOIN t_galeriemodeletypetest
ON gar_gtt_id = t_galerieresultat.xxx_id
JOIN t_donneedico AS tdd2
ON gar_premiere_lecture = tdd2.xxx_id
JOIN t_donneedico AS tdd3
ON gar_seconde_lecture = tdd3.xxx_id;
