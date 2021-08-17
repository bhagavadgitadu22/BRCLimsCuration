DROP TABLE IF EXISTS taxos_completes;

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
) SELECT xxx_id, ARRAY_TO_STRING(name_path, ' ') AS path
INTO TEMPORARY TABLE taxos_completes
FROM children;

SELECT alerte, path, iden FROM 

(SELECT don_lib as alerte, unnest(ids) AS iden, unnest(taxos) AS taxo FROM
(SELECT don_lib, array_agg(t_souche.sch_identifiant) AS ids, array_agg(t_souche.sch_taxonomie) AS taxos
FROM t_alerte_souche 
JOIN t_donneedico ON als_alerte = t_donneedico.xxx_id
JOIN t_souche ON als_sch_id = t_souche.xxx_id
WHERE don_dic_id IN (2698)
AND sch_type_souche = 3752
GROUP BY t_donneedico.xxx_id 
LIMIT 1 OFFSET 16) AS a
 
) as b
LEFT JOIN taxos_completes
ON b.taxo = taxos_completes.xxx_id

ORDER BY path;