DROP TABLE IF EXISTS ids_bacillus_a_changer;

SELECT species.xxx_id AS id_divers, genus.xxx_id AS new_sch_taxonomie,
species.don_code AS old_don_parent, genus.don_code AS new_don_parent
INTO TEMPORARY TABLE ids_bacillus_a_changer
FROM t_donneedico as species
JOIN t_souche
ON species.xxx_id = sch_taxonomie
JOIN t_donneedico as genus
ON genus.don_code = species.don_parent
JOIN t_donneedico as genus0
ON genus0.don_code = genus.don_parent
WHERE species.don_dic_id = 3755 AND genus.don_dic_id = 3755
AND genus0.don_lib = 'Bacillus' AND genus.don_lib = 'proche';

-- on remplace les id pointant vers null par les ids parents dans t_souche
UPDATE t_souche
SET sch_taxonomie = new_sch_taxonomie
FROM ids_bacillus_a_changer
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_taxonomie = id_divers
AND sch_taxonomie != new_sch_taxonomie;

UPDATE t_souche
SET sch_taxonomie = NULL
FROM ids_bacillus_a_changer
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_taxonomie = id_divers
AND sch_taxonomie = new_sch_taxonomie;

-- on redirige les don_parent des enfants de null vers les parents de null
UPDATE t_donneedico
SET don_parent = new_don_parent
FROM ids_bacillus_a_changer
WHERE don_dic_id = 3755
AND xxx_sup_dat IS NULL
AND don_parent = old_don_parent;

-- puis on supprime les vieux ids valant NULL dans t_donneedico
UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE don_dic_id = 3755
AND xxx_id IN (SELECT id_divers FROM ids_bacillus_a_changer);

DROP TABLE IF EXISTS ids_bacillus_a_changer;
