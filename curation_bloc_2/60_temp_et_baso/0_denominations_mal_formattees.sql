SELECT sch_denomination, regexp_replace(trim(sch_denomination), '[ ]+', ' ', 'g') 
FROM t_souche
WHERE xxx_id IN (SELECT	xxx_id FROM souches_groupe_cip)
AND sch_denomination SIMILAR TO '[ ]*[A-Z]{1}[a-z]+[ ]+[a-z]+([ ]+[a-z]+)*'
AND sch_denomination != regexp_replace(trim(sch_denomination), '[ ]+', ' ', 'g');

UPDATE t_souche
SET sch_denomination = regexp_replace(trim(sch_denomination), '[ ]+', ' ', 'g') 
WHERE xxx_id IN (SELECT	xxx_id FROM souches_groupe_cip)
AND sch_denomination SIMILAR TO '[ ]*[A-Z]{1}[a-z]+[ ]+[a-z]+([ ]+[a-z]+)*'
AND sch_denomination != regexp_replace(trim(sch_denomination), '[ ]+', ' ', 'g');
