SELECT sch_identifiant
FROM t_souche
WHERE sch_identifiant 
SIMILAR TO '%2[0-9]{5}%';