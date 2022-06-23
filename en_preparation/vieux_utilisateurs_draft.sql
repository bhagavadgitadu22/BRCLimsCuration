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



SELECT xxx_id, usr_nom, usr_prenom
FROM t_utilisateur
WHERE (usr_nom, usr_prenom) IN (('ANDRIAKOTO 2', 'Nirina'), 
								('ANDRIAKOTO 3', 'Nirina'),
								('BIZET 2', 'Chantal'),
								('CABANEL 2', 'Nicolas'),
								('CHATAIGNER 2', 'Anne-Sophie'),
								('Clermont', 'D.'),
								('COUTELLIER 2', 'Sabrina'),
								('COUTELLIER 3', 'Sabrina'),
								('DELANNOY-VIEILLARD', 'ICARE'),
								('MOTREFF 2', 'Laurence'),
								('Novakowski', 'administrateur'),
								('VANDEKERKHOVE 2', 'Jessy')
							   );
							   
SELECT xxx_id, usr_nom, usr_prenom 
FROM t_utilisateur
WHERE (usr_nom, usr_prenom) IN (('ANDRIAKOTO', 'Nirina'),
								('BIZET', 'Chantal'),
								('CABANEL', 'Nicolas'),
								('CHATAIGNER', 'Anne-Sophie'),
								('CLERMONT', 'Dominique'),
								('COUTELLIER', 'Sabrina'),
								('DELANNOY-VIEILLARD', 'Anne-Sophie'),
								('MOTREFF', 'Laurence'),
								('Novakowski', 'M.'),
								('VANDEKERKHOVE', 'Jessy')
							   );

DELETE FROM t_utilisateurgrp_utilisateur
WHERE ugu_usr_id IN (SELECT xxx_id FROM doublons_utilisateurs);

DELETE FROM t_utilisateur 
WHERE xxx_id IN (SELECT xxx_id FROM doublons_utilisateurs);
