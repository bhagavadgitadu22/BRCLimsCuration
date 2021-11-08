DROP TABLE IF EXISTS ids_pas_ok;

-- d'abord on récupère la liste des ids null et du premier id ancêtre non null pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_lib::text]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND xxx_sup_dat IS NULL
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.don_lib::text)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755 AND tdd.xxx_sup_dat IS NULL)
) SELECT level, xxx_id AS sch_taxonomie, don_lib, ARRAY_TO_STRING(name_path, ' > ') AS path
INTO TEMPORARY TABLE ids_pas_ok
FROM children
WHERE (level = 0 AND name_path[1] NOT IN (SELECT genus_name FROM taxonomy WHERE genus_name IS NOT NULL))
	OR (level = 1 AND (name_path[1], name_path[2]) NOT IN (SELECT genus_name, sp_epithet FROM taxonomy WHERE genus_name IS NOT NULL AND sp_epithet IS NOT NULL))
	OR (level = 2 AND (name_path[1], name_path[2], name_path[3]) NOT IN (SELECT genus_name, sp_epithet, subsp_epithet FROM taxonomy WHERE sp_epithet IS NOT NULL AND subsp_epithet IS NOT NULL))
	OR level > 2
ORDER BY level, don_lib;

UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (SELECT ids_pas_ok.sch_taxonomie
FROM ids_pas_ok
LEFT JOIN t_souche
ON ids_pas_ok.sch_taxonomie = t_souche.sch_taxonomie
WHERE t_souche.sch_taxonomie IS NULL);

DROP TABLE IF EXISTS ids_pas_ok;
