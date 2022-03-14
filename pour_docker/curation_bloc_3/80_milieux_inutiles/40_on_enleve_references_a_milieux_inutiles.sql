DROP TABLE IF EXISTS milieux_souches_a_changer;

-- on récupère les associations milieu-souche qui n'existent pas encore (et qu'un seul exemplaire de chaque association)
SELECT msc_sch_id, (ARRAY_AGG(id_numero))[1] AS id_numero, id_remplacant
INTO milieux_souches_a_changer
FROM t_milieu_souche
JOIN milieux_non_vides
ON msc_mil_id = id_numero
WHERE (msc_sch_id, id_remplacant) NOT IN (SELECT msc_sch_id, msc_mil_id FROM t_milieu_souche)
GROUP BY msc_sch_id, id_remplacant
ORDER BY COUNT(*) DESC;

-- on met à jour ces associations
UPDATE t_milieu_souche
SET msc_mil_id = id_remplacant
FROM milieux_souches_a_changer
WHERE msc_mil_id = id_numero
AND t_milieu_souche.msc_sch_id = milieux_souches_a_changer.msc_sch_id;

-- on supprime les éléments de milieu souche qui mis à jour seraient une association déjà existante donc sont inutiles
DELETE FROM t_milieu_souche
USING milieux_non_vides
WHERE msc_mil_id = id_numero;
