DROP TABLE IF EXISTS ids_dicos_taxonomie;

-- d'abord on récupère la liste des dérivés de species et du premier id ancêtre non species pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[xxx_id]::integer[]
	FROM
		t_donneedico
	WHERE
		don_dic_id IN (SELECT * FROM ids_dicos_taxonomie) 
		AND (don_lib NOT IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece')
			 OR (don_lib IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece') AND don_parent = 0))
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.xxx_id)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755
			AND tdd.don_lib IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece'))
) SELECT xxx_id AS sch_taxonomie, name_path[1] AS new_sch_taxonomie
INTO TEMPORARY TABLE ids_sp_a_changer 
FROM children
WHERE don_lib IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece')
ORDER BY new_sch_taxonomie;

-- ensuite pour chacun d'entre eux on récupère la liste de ses descendants non sp
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[xxx_id]::integer[]
	FROM
		t_donneedico
	WHERE
		don_dic_id IN (SELECT * FROM ids_dicos_taxonomie) 
		AND (don_lib NOT IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece')
			 OR (don_lib IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece') AND don_parent = 0))
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.xxx_id)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755
			AND tdd.don_lib IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece'))
) SELECT xxx_id AS sch_taxonomie, name_path[1] AS new_sch_taxonomie
INTO TEMPORARY TABLE ids_post_sp_a_changer 
FROM children
WHERE don_lib IN ('sp.', 'species', 'sp', 'spp.', 'sp. pas de souche', 'sp.pas de souche', 'sp BEN 1', 'sp BEN1', 'species 3', 'Espece')
ORDER BY new_sch_taxonomie;