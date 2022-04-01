SELECT t_souche.xxx_id, sch_identifiant, sch_version, array_to_string(ARRAY_AGG(don_lib), ', ') AS alertes
FROM t_souche
JOIN t_alerte_souche
ON als_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON als_alerte = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM ids_mots)
GROUP BY t_souche.xxx_id, sch_identifiant, sch_version
ORDER BY t_souche.xxx_id;

SELECT t_souche.xxx_id, t_souche.sch_identifiant, t_souche.sch_version, 
t_souche2.xxx_id, t_souche2.sch_identifiant, t_souche2.sch_version, 
array_to_string(ARRAY_AGG(don_lib), ', ') AS cousins
FROM t_souche
JOIN t_cousinage
ON sch_id_principal = t_souche.xxx_id
JOIN t_souche AS t_souche2
ON sch_id_secondaire = t_souche.xxx_id
JOIN t_donneedico
ON cou_type = t_donneedico.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM ids_mots)
OR t_souche2.xxx_id IN (SELECT xxx_id FROM ids_mots)
GROUP BY t_souche.xxx_id, t_souche.sch_identifiant, t_souche.sch_version, 
t_souche2.xxx_id, t_souche2.sch_identifiant, t_souche2.sch_version
ORDER BY t_souche.xxx_id;
