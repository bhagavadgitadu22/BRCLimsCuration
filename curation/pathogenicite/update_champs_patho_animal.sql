-- rediriger ea1 vers Ea1
UPDATE t_souche
SET sch_patho_animal = 72880
WHERE sch_patho_animal = 167785;

-- puis on supprime ea1
DELETE FROM t_donneedico
WHERE xxx_id = 167785;

-- de même pour les riens
UPDATE t_souche
SET sch_patho_animal = NULL
WHERE sch_patho_animal = 73439;

-- puis on supprime entrée rien
DELETE FROM t_donneedico
WHERE xxx_id = 73439;