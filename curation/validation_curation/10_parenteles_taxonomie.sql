DROP TABLE IF EXISTS chemins_taxonomie;

-- d'abord on récupère la liste des ids null et du premier id ancêtre non null pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path, don_dic_id) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_lib::text], don_dic_id
	FROM
		t_donneedico
	WHERE don_dic_id IN (SELECT xxx_id FROM t_dico WHERE dic_nom = 'Taxonomie')
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.don_lib::text), tdd.don_dic_id
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent AND t0.don_dic_id = tdd.don_dic_id)
) SELECT level, children.xxx_id AS sch_taxonomie, don_lib, ARRAY_TO_STRING(name_path, ' > ') AS path, don_dic_id, 
(regexp_matches(dic_grp_collection, '\[([0-9]+)\]'))[1]::integer AS grp_collection
INTO chemins_taxonomie
FROM children
JOIN t_dico
ON don_dic_id = t_dico.xxx_id
ORDER BY level, don_lib;
