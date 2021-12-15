SELECT sch_identifiant, sch_lieu, sch_lieu_precis 
FROM t_souche 
LEFT JOIN t_donneedico
ON t_donneedico.xxx_id = sch_lieu
WHERE t_donneedico.xxx_id IS NULL
AND sch_lieu_precis IS NOT NULL
AND sch_lieu_precis != ''
AND (sch_identifiant LIKE '%CIP%'
OR sch_identifiant LIKE '%CRBIP%')

-- 1889 SB
-- 32 CIP ou CRBIP
-- 5 PCC
-- 2 trucs bizarres C7 et G9
