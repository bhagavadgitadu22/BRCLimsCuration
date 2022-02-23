DROP TABLE IF EXISTS ids_divers_a_changer;

WITH RECURSIVE children (xxx_id, don_lib, level, don_code, don_parent, int_path, str_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, don_parent, ARRAY[xxx_id]::integer[], ARRAY[don_lib]::text[]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND xxx_sup_dat IS NULL
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, tdd.don_parent, ARRAY_APPEND(t0.int_path, tdd.xxx_id), ARRAY_APPEND(t0.str_path, tdd.don_lib::text)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755
		 	AND tdd.xxx_sup_dat IS NULL)
) SELECT xxx_id AS id_divers, int_path[2] AS new_sch_taxonomie, 
don_code AS old_don_parent, don_parent AS new_don_parent,
int_path, str_path
INTO TABLE ids_divers_a_changer
FROM children
WHERE str_path[1] = 'Photorhabdus'
AND str_path[2] IN ('asymbiotica', 'luminescens', 'temperata')
AND array_length(str_path, 1) = 3;

-- on remplace les id pointant vers null par les ids parents dans t_souche
UPDATE t_souche
SET sch_taxonomie = new_sch_taxonomie
FROM ids_divers_a_changer
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_taxonomie = id_divers
AND sch_taxonomie != new_sch_taxonomie;

-- puis on supprime les vieux ids valant NULL dans t_donneedico
UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE don_dic_id = 3755
AND xxx_id IN (SELECT id_divers FROM ids_divers_a_changer);
