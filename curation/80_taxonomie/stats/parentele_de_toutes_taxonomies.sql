DROP TABLE IF EXISTS ids_ok;

-- d'abord on récupère la liste des ids null et du premier id ancêtre non null pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_lib::text]
	FROM
		t_donneedico
	WHERE
		don_dic_id IN (3755)
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.don_lib::text)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id IN (3755))
) SELECT level, xxx_id AS sch_taxonomie, don_lib, ARRAY_TO_STRING(name_path, ' > ') AS path
FROM children
ORDER BY level, don_lib;

