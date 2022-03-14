SELECT sch_col_id, col_clg_id, col_nom, COUNT(*)
FROM t_souche 
JOIN all_strains 
ON all_strains.xxx_id = t_souche.xxx_id 
JOIN t_collection ON sch_col_id = t_collection.xxx_id
GROUP BY sch_col_id, col_clg_id, col_nom
ORDER BY COUNT(*) DESC;
