SELECT COUNT(*) FROM
(SELECT genus.don_lib
FROM t_donneedico AS genus
WHERE genus.don_dic_id = 3755) AS a;
