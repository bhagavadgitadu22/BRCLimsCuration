-- on checke que tous milieux ont bien un id dans brclims
SELECT * 
FROM milieux_vides
LEFT JOIN t_milieu
ON numero = mil_numero
WHERE t_milieu.xxx_id IS NULL;

SELECT * 
FROM milieux_non_vides
LEFT JOIN t_milieu
ON numero = mil_numero
WHERE t_milieu.xxx_id IS NULL;

SELECT * 
FROM milieux_non_vides
LEFT JOIN t_milieu
ON remplacant = mil_numero
WHERE t_milieu.xxx_id IS NULL;

-- puis on insère les ids dans mes tables csv
UPDATE milieux_vides
SET id_numero = xxx_id
FROM t_milieu
WHERE numero = mil_numero;

UPDATE milieux_non_vides
SET id_numero = xxx_id
FROM t_milieu
WHERE numero = mil_numero;

UPDATE milieux_non_vides
SET id_remplacant = xxx_id
FROM t_milieu
WHERE remplacant = mil_numero;

-- on supprime milieux à modifier pas dans cip, normalement ça ne change rien
DELETE FROM milieux_vides
WHERE id_numero IN (SELECT xxx_id FROM t_milieu WHERE mil_clg_id != 401);

DELETE FROM milieux_non_vides
WHERE id_numero IN (SELECT xxx_id FROM t_milieu WHERE mil_clg_id != 401);

DELETE FROM milieux_non_vides
WHERE id_remplacant IN (SELECT xxx_id FROM t_milieu WHERE mil_clg_id != 401);
