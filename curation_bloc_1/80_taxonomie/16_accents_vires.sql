-- on élimine les accents 
CREATE EXTENSION IF NOT EXISTS unaccent;

UPDATE t_donneedico
SET don_lib = unaccent(don_lib)
WHERE don_dic_id = 3755
AND xxx_sup_dat IS NULL
AND don_lib != unaccent(don_lib);