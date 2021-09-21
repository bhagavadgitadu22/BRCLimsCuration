SELECT * FROM
(SELECT sch_identifiant 
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND (sch_identifiant SIMILAR TO 'CIP A[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{2}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{1}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP 1[0-9]{5}T?')
ORDER BY random()
LIMIT 1000) AS a
ORDER BY custom_sort(sch_identifiant);