SELECT COUNT(*) FROM
(SELECT don_lib
FROM t_donneedico
JOIN t_souche
ON sch_lieu = t_donneedico.xxx_id
WHERE don_dic_id IN (3758)
AND don_lib IN (SELECT name_en FROM world)) AS a;
