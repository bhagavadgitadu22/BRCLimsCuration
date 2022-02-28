DELETE FROM t_alerte_souche
USING ids_mots
WHERE als_sch_id IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_cousinage
USING ids_mots
WHERE sch_id_principal IN (SELECT xxx_id FROM ids_mots)
OR sch_id_secondaire IN (SELECT xxx_id FROM ids_mots);

DELETE FROM t_souche
WHERE sch_mot IS True;

SELECT t_souche.xxx_id, sch_identifiant, sch_version, array_to_string(ARRAY_AGG(don_lib), ', ') AS alertes
FROM t_souche
JOIN t_alerte_souche
ON als_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON als_alerte = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM ids_mots)
GROUP BY t_souche.xxx_id, sch_identifiant, sch_version
ORDER BY t_souche.xxx_id;