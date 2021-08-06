UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Enterococus', 'Enterococcus')
WHERE don_lib LIKE '%Enterococus%';

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Enteroc.', 'Enterococcus')
WHERE don_lib LIKE '%Enteroc.%';

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Enteroco.', 'Enterococcus')
WHERE don_lib LIKE '%Enteroco.%';

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Entero.', 'Enterococcus ')
WHERE don_lib LIKE '%Entero.%';