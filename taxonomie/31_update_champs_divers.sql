-- on définit la liste des éléments à supprimer
DROP TABLE IF EXISTS elements_inutiles;

CREATE TEMPORARY TABLE elements_inutiles(
   column_list text
);

INSERT INTO elements_inutiles (column_list) VALUES
('Espece'), (' '), ('pas de souche'), ('like'), ('bacterium'), 
('Unnamed'), ('Bacterium'), ('Carlier'), ('Jean Philippe'), ('Inconnue'), 
('???'), ('Candidatus'), ('Corynéformes'), ('uncertain'), ('unnamed'),
('Unindentified'), ('102303'), ('109135'), ('Crynéformes'), ('ESSAI 100000'), 
('ESSAI 100001'), ('Genre'), ('Ommited'), ('Unnamed bacterium'), ('jetÇe'),
('Unidentified'), ('SP group'), ('pas d''ampoule'), ('PAS DE SOUCHE'), ('Uncertain'),
('Unknown acetogenic'), ('proche'), ('Coryneformes'), ('Cryneformes'), ('ungrouped 1271'),
('ungrouped 640');

-- on supprime les tables temporaires créées au dernier lancement de ce script
DROP TABLE IF EXISTS ids_sp_a_changer;
DROP TABLE IF EXISTS ids_post_sp_a_changer;

-- d'abord on récupère la liste des dérivés de species et du premier id ancêtre non species pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[xxx_id]::integer[]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND (don_lib NOT IN (SELECT * FROM elements_inutiles)
			 OR (don_lib IN (SELECT * FROM elements_inutiles) AND don_parent = 0))
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.xxx_id)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755
			AND tdd.don_lib IN (SELECT * FROM elements_inutiles))
) SELECT xxx_id AS id_sp, name_path[1] AS new_sch_taxonomie
INTO TEMPORARY TABLE ids_sp_a_changer 
FROM children
WHERE don_lib IN (SELECT * FROM elements_inutiles)
ORDER BY new_sch_taxonomie;

-- ensuite pour chacun d'entre eux on récupère la liste de ses descendants non sp
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_parent]::integer[]
	FROM
		t_donneedico
	WHERE
		xxx_id IN (SELECT id_sp FROM ids_sp_a_changer)
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.don_parent)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755)
) SELECT DISTINCT xxx_id AS id_enfant, name_path[1] AS new_don_parent
INTO TEMPORARY TABLE ids_post_sp_a_changer 
FROM children
ORDER BY new_don_parent;

-- on remplace les id pointant vers null par les ids parents dans t_souche
UPDATE t_souche
SET sch_taxonomie = new_sch_taxonomie
FROM ids_sp_a_changer
WHERE sch_taxonomie = id_sp
AND sch_taxonomie != new_sch_taxonomie;

UPDATE t_souche
SET sch_taxonomie = NULL
FROM ids_sp_a_changer
WHERE sch_taxonomie = id_sp
AND sch_taxonomie = new_sch_taxonomie;

-- on redirige les don_parent des enfants de null vers les parents de null
UPDATE t_donneedico
SET don_parent = new_don_parent
FROM ids_post_sp_a_changer
WHERE xxx_id = id_enfant;

-- puis on supprime les vieux ids valant NULL dans t_donneedico
DELETE FROM t_donneedico
WHERE xxx_id IN (SELECT id_sp FROM ids_sp_a_changer);

DROP TABLE IF EXISTS ids_sp_a_changer;
DROP TABLE IF EXISTS ids_post_sp_a_changer;