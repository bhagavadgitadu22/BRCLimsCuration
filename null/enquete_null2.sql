SELECT xxx_id
FROM t_souche
WHERE sch_cpt_id::text LIKE ANY
(SELECT xxx_id::text
FROM t_donneedico
WHERE don_dic_id IN (791931, 789602, 790830, 791324)
AND don_lib NOT IN ('NULL', ' '));

