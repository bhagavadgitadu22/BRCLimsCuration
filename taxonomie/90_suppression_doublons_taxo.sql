DROP TABLE IF EXISTS ids_doubles;

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

/* dans la table t_souches on repointe tous les ids de taxo valant un id1 vers le id2 correspondant */
UPDATE t_souche
SET sch_taxonomie = id2
FROM ids_doubles
WHERE sch_taxonomie = id1;

/* puis on peut supprimer les id1 dans la table t_donneedico */
DELETE FROM t_donneedico WHERE t_donneedico.xxx_id IN (SELECT id1 FROM ids_doubles);

/* enfin on supprime la table temporaire où l'on stockait ces id1 et 2 */
DROP TABLE ids_doubles;