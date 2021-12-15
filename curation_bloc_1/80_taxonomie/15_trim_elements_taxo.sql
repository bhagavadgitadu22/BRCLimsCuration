-- on trime les éléments de taxonomie pour virer les espaces inutiles
UPDATE t_donneedico
SET don_lib = TRIM(don_lib)
WHERE don_dic_id = 3755
AND xxx_sup_dat IS NULL;