-- on récupère les lieux où un pays est présent
SELECT a.xxx_id, don_lib, (array_agg(a.name_en))[1] AS pays

FROM (SELECT xxx_id, don_lib, name_en
FROM t_donneedico
JOIN world
ON don_lib LIKE CONCAT('%', name_en, '%')
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND don_lib != name_en
AND don_lib NOT SIMILAR TO CONCAT('%', name_en, '[a-zA-Z]%')
AND don_lib NOT SIMILAR TO CONCAT('%[a-zA-Z]', name_en, '%')) AS a

GROUP BY a.xxx_id, don_lib
HAVING COUNT(*) = 1;
