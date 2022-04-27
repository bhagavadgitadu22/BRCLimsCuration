DROP TABLE IF EXISTS new_collection;

SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_autres_coll, CONCAT(col_descr, CASE 
	WHEN col_descr!= col_nom THEN CONCAT(' (', col_nom, ')')
	ELSE ''
END) AS coll
INTO new_collection
FROM t_souche
JOIN t_collection
ON sch_col_id = t_collection.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip);

UPDATE t_souche
SET sch_autres_coll = CASE 
	WHEN t_souche.sch_autres_coll = '' THEN coll
	ELSE CONCAT(t_souche.sch_autres_coll, ';', coll)
END
FROM new_collection
WHERE t_souche.xxx_id = new_collection.xxx_id;
