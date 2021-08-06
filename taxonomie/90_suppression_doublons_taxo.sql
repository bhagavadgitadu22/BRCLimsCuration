DROP TABLE IF EXISTS ids_doubles;
DROP TABLE IF EXISTS parents_doubles;

/* d'abord on regarde la liste des taxos en double */
SELECT t_donneedico.xxx_id AS id1, id2 
INTO TEMPORARY TABLE ids_doubles
FROM t_donneedico JOIN

(SELECT don_lib, PERCENTILE_DISC(0) WITHIN GROUP (ORDER BY xxx_id) AS id2, COUNT(*)
FROM t_donneedico
WHERE don_dic_id = 3755
GROUP BY don_lib
HAVING COUNT(*) > 1) AS duplicates

ON t_donneedico.don_lib = duplicates.don_lib
WHERE t_donneedico.don_dic_id = 3755
AND t_donneedico.xxx_id != id2
ORDER BY duplicates.don_lib;

/* on récupère le don_code des id1 et des id2 */
SELECT tdd1.don_code AS old_don_parent, tdd2.don_code AS new_don_parent
INTO parents_doubles
FROM t_donneedico AS tdd1, t_donneedico AS tdd2
WHERE (tdd1.xxx_id, tdd2.xxx_id) IN (SELECT id1, id2 FROM ids_doubles);

-- et on associe les enfants des id1 aux id2
UPDATE t_donneedico
SET don_parent = new_don_parent
FROM parents_doubles
WHERE don_parent = old_don_parent;

/* dans la table t_souches on repointe tous les ids de taxo valant un id1 vers le id2 correspondant */
UPDATE t_souche
SET sch_taxonomie = id2
FROM ids_doubles
WHERE sch_taxonomie = id1;

/* puis on peut supprimer les id1 dans la table t_donneedico */
DELETE FROM t_donneedico WHERE t_donneedico.xxx_id IN (SELECT id1 FROM ids_doubles);

/* enfin on supprime la table temporaire où l'on stockait ces id1 et 2 */
DROP TABLE ids_doubles;
DROP TABLE IF EXISTS parents_doubles;