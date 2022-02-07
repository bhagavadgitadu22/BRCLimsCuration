SELECT MAX(att_position)
FROM t_attribut 
WHERE att_col_id  IN
(SELECT xxx_id
FROM t_collection
WHERE col_clg_id = 401)
AND att_filtre = 'IDENTITY'
