DROP TABLE IF EXISTS ids_a_changer;

/* d'abord on regarde les lieux qui comportent plusieurs ids
on garde la liste de tous les doublons dans id1 et l'id à l'origine de ces doublons dans id2 */
SELECT t_donneedico.xxx_id AS id1, id2 
INTO TEMPORARY TABLE ids_a_changer
FROM t_donneedico JOIN

(SELECT a.don_lib, 
 (array_agg(a.xxx_id))[1] AS id2, 
 COUNT(*) AS number_of_duplicates FROM 
 
(SELECT t_donneedico.xxx_id, t_donneedico.don_lib
FROM t_donneedico 
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib = 'Korea (Republic of)') AS a
 
GROUP BY a.don_lib
HAVING COUNT(*) > 1) AS duplicates

ON t_donneedico.don_lib = duplicates.don_lib
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND t_donneedico.xxx_id != id2;

/* dans la table t_souches on repointe tous les ids de lieux valant un id1 vers le id2 correspondant */
UPDATE t_souche AS sch
SET sch_lieu = id2
FROM ids_a_changer
WHERE sch.sch_lieu = ids_a_changer.id1
AND sch.xxx_sup_dat IS NULL;

/* puis on peut supprimer les id1 dans la table t_donneedico */
UPDATE t_donneedico 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE t_donneedico.xxx_id IN (SELECT id1 FROM ids_a_changer);

/* enfin on supprime la table temporaire où l'on stockait ces id1 et 2 */
DROP TABLE IF EXISTS ids_a_changer;
