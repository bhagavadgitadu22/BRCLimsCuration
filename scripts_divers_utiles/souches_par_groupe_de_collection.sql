SELECT clg_nom, clg_descr, array_agg(sch_identifiant), array_agg(col_nom), COUNT(*)
FROM t_souche
JOIN t_collection
ON sch_col_id = t_collection.xxx_id
JOIN t_collectiongrp
ON col_clg_id = t_collectiongrp.xxx_id
WHERE col_nom != 'CIP'
GROUP BY clg_nom, clg_descr
ORDER BY COUNT(*) DESC;
