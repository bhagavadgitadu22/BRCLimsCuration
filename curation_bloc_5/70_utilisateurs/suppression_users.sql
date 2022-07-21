DROP TABLE IF EXISTS doublons_utilisateurs;

CREATE TABLE doublons_utilisateurs (
	new_id int,
	old_id int
);

INSERT INTO doublons_utilisateurs VALUES
(1200, 1221),
(1273, 1318),
(1197, 1321),
(1203, 1296),
(1203, 1309),
(1223, 1224),
(1237, 1304),
(1266, 1295),
(1275, 1276),
(1286, 1297),
(1286, 1311),
(1294, 1319);

DELETE FROM t_utilisateurgrp_utilisateur
WHERE ugu_usr_id IN (SELECT old_id FROM doublons_utilisateurs);

UPDATE t_souche
SET xxx_cre_usr_id = new_id
FROM doublons_utilisateurs
WHERE xxx_cre_usr_id = old_id;

UPDATE t_souche
SET xxx_maj_usr_id = new_id
FROM doublons_utilisateurs
WHERE xxx_maj_usr_id = old_id;

UPDATE t_souche
SET xxx_sup_usr_id = new_id
FROM doublons_utilisateurs
WHERE xxx_sup_usr_id = old_id;

UPDATE t_souche
SET sch_auteur_acquisition = new_id
FROM doublons_utilisateurs
WHERE sch_auteur_acquisition = old_id;

UPDATE t_souche
SET sch_qualite_approbateur = new_id
FROM doublons_utilisateurs
WHERE sch_qualite_approbateur = old_id;

UPDATE t_planification
SET pla_usr_id = new_id
FROM doublons_utilisateurs
WHERE pla_usr_id = old_id;

DELETE FROM t_utilisateur 
WHERE xxx_id IN (SELECT old_id FROM doublons_utilisateurs);
