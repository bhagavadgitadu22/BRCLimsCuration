SELECT t_un.xxx_id, t_un.sch_identifiant, t_deux.xxx_id, t_deux.sch_identifiant
FROM t_alerte_souche
JOIN t_souche AS t_un
ON sch_id_principal = t_un.xxx_id
JOIN t_souche AS t_deux
ON sch_id_secondaire = t_deux.xxx_id
WHERE t_un.xxx_id != t_deux.xxx_id;
