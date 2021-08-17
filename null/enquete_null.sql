SELECT sch_identifiant
FROM t_souche
WHERE t_souche::text LIKE ANY
(SELECT CONCAT('%', don_lib, '%') FROM t_donneedico
WHERE don_dic_id IN (791931, 789602, 790830, 791324))