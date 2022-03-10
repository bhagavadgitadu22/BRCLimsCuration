SELECT DISTINCT sch_identifiant 
FROM t_souche
WHERE sch_col_id IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND sch_identifiant NOT SIMILAR TO 'CIP A[0-9]+T?'
AND sch_identifiant NOT SIMILAR TO 'CIP [0-9]{2}.[0-9]+T?'
AND sch_identifiant NOT SIMILAR TO 'CIP [0-9]{1}.[0-9]+T?'
AND sch_identifiant NOT SIMILAR TO 'CIP 1[0-9]{5}T?'
AND sch_identifiant NOT SIMILAR TO 'CIP 2[0-9]{5}T?'
AND sch_identifiant NOT SIMILAR TO 'CRBIP[0-9]{2}.[0-9]+T?'
AND sch_identifiant NOT SIMILAR TO 'CRBIP[0-9]{1}.[0-9]+T?';
