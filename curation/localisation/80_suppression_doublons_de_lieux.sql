DROP TABLE ids_a_changer;

/* d'abord on regarde les lieux qui comportent plusieurs ids
on garde la liste de tous les doublons dans id1 et l'id à l'origine de ces doublons dans id2 */
SELECT t_donneedico.xxx_id AS id1, id2 
INTO TEMPORARY TABLE ids_a_changer
FROM t_donneedico JOIN

(SELECT a.don_lib, percentile_disc(0) WITHIN GROUP (ORDER BY a.xxx_id) AS id2, COUNT(*) AS number_of_duplicates FROM 
(SELECT t_donneedico.xxx_id, t_donneedico.don_lib, 
 COUNT(*) AS number_of_uses FROM t_donneedico 
JOIN t_souche 
ON t_donneedico.xxx_id = t_souche.sch_lieu
GROUP BY t_donneedico.xxx_id) AS a
GROUP BY a.don_lib
HAVING COUNT(*) > 1) AS duplicates

ON t_donneedico.don_lib = duplicates.don_lib
WHERE t_donneedico.xxx_id != id2
ORDER BY duplicates.don_lib;

/* dans la table t_souches on repointe tous les ids de lieux valant un id1 vers le id2 correspondant */
UPDATE t_souche AS sch
SET sch_lieu = id2
FROM ids_a_changer
WHERE sch.sch_lieu = ids_a_changer.id1;

/* puis on peut supprimer les id1 dans la table t_donneedico */
DELETE FROM t_donneedico WHERE t_donneedico.xxx_id IN (SELECT id1 FROM ids_a_changer);

/* enfin on supprime la table temporaire où l'on stockait ces id1 et 2 */
DROP TABLE ids_a_changer;