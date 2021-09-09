-- remplacer les riens de pathogenicite par des 1

-- d'abord ajouter un 1 dans t_pathogenicite
INSERT INTO t_pathogenicite (xxx_vbloc, xxx_brc_id, pto_lib, pto_alarme)
VALUES (0, 1, '1', FALSE)
ON CONFLICT (xxx_brc_id, pto_lib)
DO NOTHING;

-- puis mettre à jour tous les riens pour mettre 1 à la place
UPDATE t_souche
SET sch_pto_id = (SELECT t_pathogenicite.xxx_id FROM t_pathogenicite WHERE t_pathogenicite.pto_lib = '1')
WHERE sch_pto_id IS NULL;