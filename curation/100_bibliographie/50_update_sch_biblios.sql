DROP TABLE IF EXISTS new_biblios;

SELECT sch_identifiant, array_to_string(ARRAY_AGG(string_doc ORDER BY n_ligne), E';\n') AS new_biblio
INTO TEMPORARY TABLE new_biblios
FROM all_documents
GROUP BY sch_identifiant;

UPDATE t_souche
SET sch_bibliographie = new_biblio
FROM new_biblios
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_souche.sch_identifiant = new_biblios.sch_identifiant;
