DROP TABLE IF EXISTS ids_a_changer;

/* d'abord on regarde les lieux qui comportent plusieurs ids
on garde la liste de tous les doublons dans id1 et l'id à l'origine de ces doublons dans id2 */
SELECT t_donneedico.xxx_id AS id1, id2,
t_donneedico.don_lib AS version_1, duplicates.don_lib AS version_2

INTO TABLE ids_a_changer

FROM t_donneedico JOIN

(SELECT a.don_lib, 
 (array_agg(a.xxx_id))[1] AS id2, 
 COUNT(*) AS number_of_duplicates FROM 
 
(SELECT t_donneedico.xxx_id, t_donneedico.don_lib, 
COUNT(*) AS number_of_uses FROM t_donneedico 
WHERE don_dic_id = 104
AND xxx_sup_dat IS NULL
GROUP BY t_donneedico.xxx_id) AS a
 
GROUP BY a.don_lib
HAVING COUNT(*) > 1) AS duplicates

ON t_donneedico.don_lib = duplicates.don_lib
WHERE don_dic_id = 104
AND xxx_sup_dat IS NULL
AND t_donneedico.xxx_id != id2
ORDER BY duplicates.don_lib;

/* dans la table t_souches on repointe tous les ids de lieux valant un id1 vers le id2 correspondant */
UPDATE t_souche AS sch
SET sch_lieu = id2
FROM ids_a_changer
WHERE sch.sch_depositaire = ids_a_changer.id1
AND sch.xxx_sup_dat IS NULL;

/* puis on peut supprimer les id1 dans la table t_donneedico */
UPDATE t_donneedico 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE t_donneedico.xxx_id IN (SELECT id1 FROM ids_a_changer);
