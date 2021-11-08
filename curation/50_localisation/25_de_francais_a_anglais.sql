-- on traduit en anglais les entrées de dico avec des noms de pays en français
DROP TABLE IF EXISTS ids_lieux_a_traduire;

-- on récupère les ids de lieux dans donnee_dico qui contenait un nom en français
SELECT t_donneedico.xxx_id AS id_lieu, name_fr, name_en
INTO TEMPORARY TABLE ids_lieux_a_traduire
FROM t_donneedico
JOIN world
ON t_donneedico.don_lib LIKE CONCAT('%', world.name_fr, '%')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND world.name_en NOT LIKE CONCAT('%', world.name_fr, '%');

-- on remplace les noms français par des noms anglais dans la liste des lieux dans t_donneedico
UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, name_fr, name_en)
FROM ids_lieux_a_traduire
WHERE xxx_id = id_lieu;

-- on supprime la table temporaire
DROP TABLE IF EXISTS ids_lieux_a_traduire;
