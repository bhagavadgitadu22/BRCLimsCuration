-- d'abord on récupère la liste des ids null et du premier id ancêtre non null pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_lib::text]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.don_lib::text)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755)
) SELECT xxx_id AS sch_taxonomie, don_lib, ARRAY_TO_STRING(name_path, ' > ') AS path
FROM children
WHERE (level = 0 AND name_path[1] IN (SELECT genus_name FROM taxonomy))
	OR (level = 1 AND (name_path[1], name_path[2]) IN (SELECT genus_name, sp_epithet FROM taxonomy))
	OR (level = 2 AND (name_path[1], name_path[2], name_path[3]) IN (SELECT genus_name, sp_epithet, subsp_epithet FROM taxonomy))
ORDER BY xxx_id;

/*
SELECT genus.don_lib
FROM t_donneedico AS genus
WHERE genus.don_dic_id = 3755;
*/
