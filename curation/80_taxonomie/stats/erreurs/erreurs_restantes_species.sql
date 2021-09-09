DROP TABLE IF EXISTS ids_ok;

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
) SELECT level, xxx_id AS sch_taxonomie, don_lib, ARRAY_TO_STRING(name_path, ' ') AS path
INTO TEMPORARY TABLE ids_ok
FROM children
WHERE level = 1 AND (name_path[1], name_path[2]) NOT IN (SELECT genus_name, sp_epithet FROM taxonomy WHERE genus_name IS NOT NULL AND sp_epithet IS NOT NULL)
ORDER BY level, don_lib;

SELECT ids_ok.sch_taxonomie, don_lib, path, COUNT(*)
FROM ids_ok
LEFT JOIN t_souche
ON ids_ok.sch_taxonomie = t_souche.sch_taxonomie
GROUP BY ids_ok.sch_taxonomie, don_lib, path, level
ORDER BY level, COUNT(*) DESC;

/*
SELECT * 
FROM t_souche
WHERE sch_taxonomie IS NOT NULL;
*/
