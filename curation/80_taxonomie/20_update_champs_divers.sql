-- on supprime les tables temporaires créées au dernier lancement de ce script
DROP TABLE IF EXISTS elements_inutiles;
DROP TABLE IF EXISTS ids_divers_a_changer;

-- on définit la liste des éléments à supprimer
CREATE TEMPORARY TABLE elements_inutiles(
   column_list text
);

INSERT INTO elements_inutiles (column_list) VALUES
('NULL'), (''),

('sp.'), ('species'), ('sp'), ('spp.'), ('sp. pas de souche'), 
('sp.pas de souche'), ('sp BEN 1'), ('sp BEN1'), ('species 3'),

('Espece'), (' '), ('pas de souche'), ('like'), ('bacterium'), 
('Unnamed'), ('Bacterium'), ('Carlier'), ('Jean Philippe'), ('Inconnue'), 
('???'), ('Candidatus'), ('uncertain'), ('unnamed'), ('jetCe'), 
('Unindentified'), ('102303'), ('109135'), ('Crynéformes'), ('ESSAI 100000'), 
('ESSAI 100001'), ('Genre'), ('Ommited'), ('Unnamed bacterium'), ('jetÇe'),
('Unidentified'), ('SP group'), ('pas d''ampoule'), ('PAS DE SOUCHE'), ('Uncertain'),
('Unknown acetogenic'), ('proche'), ('ungrouped 1271'), ('ungrouped 640'), ('strain'), 
('Coryneformes'), ('Cryneformes');

-- d'abord on récupère la liste des dérivés de species et du premier id ancêtre non species pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, don_parent, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, don_parent, ARRAY[xxx_id]::integer[]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND xxx_sup_dat IS NULL
		AND (don_lib NOT IN (SELECT * FROM elements_inutiles)
			 OR (don_lib IN (SELECT * FROM elements_inutiles) AND don_parent = 0))
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, tdd.don_parent, ARRAY_APPEND(t0.name_path, tdd.xxx_id)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755
		 	AND tdd.xxx_sup_dat IS NULL
			AND tdd.don_lib IN (SELECT * FROM elements_inutiles))
) SELECT xxx_id AS id_divers, name_path[1] AS new_sch_taxonomie, 
don_code AS old_don_parent, don_parent AS new_don_parent
INTO TEMPORARY TABLE ids_divers_a_changer 
FROM children
WHERE don_lib IN (SELECT * FROM elements_inutiles)
ORDER BY new_sch_taxonomie;

-- on remplace les id pointant vers null par les ids parents dans t_souche
UPDATE t_souche
SET sch_taxonomie = new_sch_taxonomie
FROM ids_divers_a_changer
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_taxonomie = id_divers
AND sch_taxonomie != new_sch_taxonomie;

UPDATE t_souche
SET sch_taxonomie = NULL
FROM ids_divers_a_changer
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_taxonomie = id_divers
AND sch_taxonomie = new_sch_taxonomie;

-- on redirige les don_parent des enfants de null vers les parents de null
UPDATE t_donneedico
SET don_parent = new_don_parent
FROM ids_divers_a_changer
WHERE don_dic_id = 3755
AND xxx_sup_dat IS NULL
AND don_parent = old_don_parent
AND don_lib NOT IN (SELECT * FROM elements_inutiles);

-- puis on supprime les vieux ids valant NULL dans t_donneedico
UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE don_dic_id = 3755
AND xxx_id IN (SELECT id_divers FROM ids_divers_a_changer);

DROP TABLE IF EXISTS elements_inutiles;
DROP TABLE IF EXISTS ids_divers_a_changer;