DROP TABLE IF EXISTS ids_nulls_a_changer;
DROP TABLE IF EXISTS ids_dicos_taxonomie;

SELECT don_dic_id
INTO TEMPORARY TABLE ids_dicos_taxonomie 
FROM t_donneedico
JOIN t_souche
ON sch_taxonomie = t_donneedico.xxx_id
GROUP BY don_dic_id;

-- d'abord on récupère la liste des ids null et du premier id ancêtre non null pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[xxx_id]::integer[]
	FROM
		t_donneedico
	WHERE
		don_dic_id IN (SELECT * FROM ids_dicos_taxonomie) AND (don_lib != 'NULL' OR (don_lib = 'NULL' AND don_parent = 0))
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, ARRAY_APPEND(t0.name_path, tdd.xxx_id)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id IN (SELECT * FROM ids_dicos_taxonomie) AND tdd.don_lib = 'NULL')
) SELECT xxx_id AS sch_taxonomie, name_path[1] AS new_sch_taxonomie 

INTO TEMPORARY TABLE ids_nulls_a_changer 

FROM children
WHERE don_lib = 'NULL'
ORDER BY xxx_id;

-- on remplace les id pointant vers null par les ids parents dans t_souche
UPDATE t_souche
SET sch_taxonomie = new_sch_taxonomie
FROM ids_nulls_a_changer
WHERE t_souche.sch_taxonomie = ids_nulls_a_changer.sch_taxonomie
AND t_souche.sch_taxonomie != ids_nulls_a_changer.new_sch_taxonomie;

UPDATE t_souche
SET sch_taxonomie = NULL
FROM ids_nulls_a_changer
WHERE t_souche.sch_taxonomie = ids_nulls_a_changer.sch_taxonomie
AND t_souche.sch_taxonomie = ids_nulls_a_changer.new_sch_taxonomie;

-- puis on supprime les vieux ids valant NULL dans t_donneedico
DELETE FROM t_donneedico
WHERE xxx_id IN (SELECT sch_taxonomie FROM ids_nulls_a_changer);

DROP TABLE IF EXISTS ids_nulls_a_changer;
DROP TABLE IF EXISTS ids_dicos_taxonomie;