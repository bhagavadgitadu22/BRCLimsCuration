UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Enterococus', 'Enterococcus')
WHERE don_lib LIKE '%Enterococus%'
AND xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Enteroc.', 'Enterococcus')
WHERE don_lib LIKE '%Enteroc.%'
AND xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Enteroco.', 'Enterococcus')
WHERE don_lib LIKE '%Enteroco.%'
AND xxx_sup_dat IS NULL;

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Entero.', 'Enterococcus ')
WHERE don_lib LIKE '%Entero.%'
AND xxx_sup_dat IS NULL;