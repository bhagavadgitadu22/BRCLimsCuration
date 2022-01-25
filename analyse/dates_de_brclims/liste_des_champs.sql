SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'public'
AND table_name = 't_souche'
AND column_name LIKE '%dat%';

SELECT DISTINCT att_nom
FROM t_attribut 
WHERE LOWER(att_nom) LIKE '%dat%'
AND att_col_id IN (SELECT xxx_id FROM t_collection WHERE col_clg_id = 401);
