DROP TABLE IF EXISTS ids_serovar;

-- d'abord on récupère la liste des ids de serovar et les ids parents
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path, id_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_lib::text], ARRAY[xxx_id::integer]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, 
		 	ARRAY_APPEND(t0.name_path, tdd.don_lib::text), ARRAY_APPEND(t0.id_path, tdd.xxx_id::integer)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755)
) SELECT xxx_id AS id_serovar, id_path[2] AS id_parent
INTO TEMPORARY TABLE ids_serovar
FROM children
WHERE level = 2 AND (name_path[1], name_path[2], name_path[3]) NOT IN (SELECT genus_name, sp_epithet, subsp_epithet FROM taxonomy WHERE subsp_epithet IS NOT NULL)
ORDER BY level, don_lib;

-- puis on redirige les souches des serovars vers les parents
UPDATE t_souche
SET sch_taxonomie = id_parent
FROM ids_serovar
WHERE sch_taxonomie = id_serovar;

-- puis on supprime les serovar
DELETE FROM t_donneedico
WHERE xxx_id IN (SELECT id_serovar FROM ids_serovar);

DROP TABLE IF EXISTS ids_serovar;
