DROP TABLE IF EXISTS lignes_historiques;
DROP TABLE IF EXISTS lignes_a_changer;
DROP TABLE IF EXISTS synthese;

SELECT xxx_id, nr AS numero_ligne, trim(arr[nr]) AS ligne
INTO TABLE lignes_historiques
FROM  (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM  (SELECT xxx_id, string_to_array(sch_historique, '<-') AS arr FROM t_souche) t
   ) sub;

SELECT xxx_id, numero_ligne, ligne,
(REGEXP_MATCHES(ligne, '\(([12]{1}[0-9]{3})\)'))[1] AS annee,
trim(REGEXP_REPLACE(ligne, '[ ]*\(([12]{1}[0-9]{3})\)[ ]*', ' ')) AS texte
INTO lignes_a_changer
FROM lignes_historiques
WHERE ligne SIMILAR TO '%\([12]{1}[0-9]{3}\)%';

UPDATE lignes_historiques
SET ligne = CONCAT(annee, ', ', texte)
FROM lignes_a_changer
WHERE lignes_historiques.xxx_id = lignes_a_changer.xxx_id
AND lignes_historiques.numero_ligne = lignes_a_changer.numero_ligne;

SELECT xxx_id, array_to_string(ARRAY_AGG(ligne ORDER BY numero_ligne), ' <- ') AS new_historique
INTO synthese
FROM lignes_historiques
GROUP BY xxx_id;

/*
SELECT sch_historique, new_historique
FROM t_souche
JOIN synthese
ON t_souche.xxx_id = synthese.xxx_id
WHERE sch_historique != new_historique;
*/

UPDATE t_souche
SET sch_historique = new_historique
FROM synthese
WHERE t_souche.xxx_id = synthese.xxx_id
AND sch_historique != new_historique;
