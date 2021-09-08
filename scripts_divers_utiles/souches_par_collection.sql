SELECT col_nom, col_descr, COUNT(*)
FROM t_souche
JOIN t_collection
ON sch_col_id = t_collection.xxx_id
GROUP BY col_nom, col_descr
ORDER BY COUNT(*) DESC;
