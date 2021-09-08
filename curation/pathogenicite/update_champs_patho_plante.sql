-- remplacer 1 par Ep1
UPDATE t_donneedico
SET don_lib = 'Ep1'
WHERE xxx_id = 101484;

-- de même de 2 vers Ep2
UPDATE t_donneedico
SET don_lib = 'Ep2'
WHERE xxx_id = 212866;

-- rediriger les riens
UPDATE t_souche
SET sch_patho_plante = NULL
WHERE sch_patho_plante = 73438;

-- puis on supprime entrée rien
DELETE FROM t_donneedico
WHERE xxx_id = 73438;

-- on met rhyzobium radiobacter en Ep1
UPDATE t_souche
SET sch_patho_plante = 101484
WHERE sch_denomination = 'Rhizobium radiobacter';