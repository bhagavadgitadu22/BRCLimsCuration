DROP TABLE IF EXISTS new_biblios;

SELECT xxx_id, array_to_string(ARRAY_AGG(string_doc ORDER BY n_ligne), E';\n') AS new_biblio
INTO TEMPORARY TABLE new_biblios
FROM all_documents
GROUP BY xxx_id;

UPDATE t_souche
SET sch_bibliographie = new_biblio
FROM new_biblios
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_souche.xxx_id = new_biblios.xxx_id
AND sch_bibliographie != new_biblio;
