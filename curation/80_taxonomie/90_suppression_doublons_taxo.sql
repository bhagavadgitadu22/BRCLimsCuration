DROP TABLE IF EXISTS genealogie;
DROP TABLE IF EXISTS ids_doubles;
DROP TABLE IF EXISTS parents_doubles;

-- d'abord on récupère la liste des dérivés de species et du premier id ancêtre non species pour chacun d'entre eux
WITH RECURSIVE children (xxx_id, don_lib, don_code, don_parent, name_path) AS (
	SELECT
		xxx_id, don_lib, don_code, don_parent, ARRAY[don_lib::text]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755 AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, tdd.don_code, tdd.don_parent, ARRAY_APPEND(t0.name_path, tdd.don_lib::text)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755)
) SELECT xxx_id, name_path
INTO TEMPORARY TABLE genealogie
FROM children;

/* d'abord on regarde la liste des taxos en double */
SELECT genealogie.xxx_id AS id1, id2 
INTO TEMPORARY TABLE ids_doubles
FROM genealogie JOIN

(SELECT name_path, PERCENTILE_DISC(0) WITHIN GROUP (ORDER BY xxx_id) AS id2, COUNT(*)
FROM genealogie
GROUP BY name_path
HAVING COUNT(*) > 1) AS duplicates

ON genealogie.name_path = duplicates.name_path
WHERE genealogie.xxx_id != id2
ORDER BY duplicates.name_path;

/* on récupère le don_code des id1 et des id2 */
SELECT tdd1.don_code AS old_don_parent, tdd2.don_code AS new_don_parent
INTO parents_doubles
FROM t_donneedico AS tdd1, t_donneedico AS tdd2
WHERE (tdd1.xxx_id, tdd2.xxx_id) IN (SELECT id1, id2 FROM ids_doubles);

/* dans la table t_souches on repointe tous les ids de taxo valant un id1 vers le id2 correspondant */
UPDATE t_souche
SET sch_taxonomie = id2
FROM ids_doubles
WHERE sch_taxonomie = id1;

-- et on associe les enfants des id1 aux id2
UPDATE t_donneedico
SET don_parent = new_don_parent
FROM parents_doubles
WHERE don_parent = old_don_parent;

/* puis on peut supprimer les id1 dans la table t_donneedico */
DELETE FROM t_donneedico WHERE t_donneedico.xxx_id IN (SELECT id1 FROM ids_doubles);

/* enfin on supprime la table temporaire où l'on stockait ces id1 et 2 */
DROP TABLE IF EXISTS genealogie;
DROP TABLE ids_doubles;
DROP TABLE IF EXISTS parents_doubles;

DROP TABLE IF EXISTS taxonomy;
