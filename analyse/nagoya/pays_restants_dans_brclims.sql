SELECT don_lib, COUNT(*)
FROM t_souche
JOIN t_donneedico
ON t_donneedico.xxx_id = sch_lieu
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND don_lib NOT LIKE '%Korea%'
AND don_lib NOT SIMILAR TO '(1964|CEI|Yugoslavia|USSR)'
AND don_lib NOT SIMILAR TO '(Africa|Asia|Europe|South America|Arctic|Antarctica)'
AND don_lib NOT SIMILAR TO '%(Sea|Ocean)%'
AND sch_mot IS False
GROUP BY don_lib
ORDER BY don_lib;
