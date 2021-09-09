SELECT sch_identifiant 
FROM souches_groupe_cip
WHERE sch_identifiant SIMILAR TO '%CIP%'
AND NOT(sch_identifiant SIMILAR TO 'CIP A[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{2}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{1}.[0-9]+T?'
OR sch_identifiant SIMILAR TO 'CIP [0-9]{6}T?');
