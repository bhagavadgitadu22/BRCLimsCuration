-- on trime les éléments de taxonomie pour virer les espaces inutiles
UPDATE t_donneedico
SET don_lib = TRIM(regexp_replace(don_lib, '\s+', ' ', 'g'))
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = TRIM(regexp_replace(don_lib, '\s+', ' ', 'g'))
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885);