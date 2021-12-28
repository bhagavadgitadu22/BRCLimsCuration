SELECT DISTINCT att_nom
FROM t_date_val
JOIN t_attribut
ON dvl_att_id = t_attribut.xxx_id
WHERE att_nom != 'Date de réception';

