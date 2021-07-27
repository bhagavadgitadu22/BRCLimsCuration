UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'U.S.A.', 'United States of America')
WHERE don_lib LIKE '%U.S.A.%' AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'USA.', 'United States of America')
WHERE don_lib LIKE '%USA.%' AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'USA', 'United States of America')
WHERE don_lib LIKE '%USA%' AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'U.K.', 'United Kingdom of Great Britain and Northern Ireland')
WHERE don_lib LIKE '%U.K.%' AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'UK', 'United Kingdom of Great Britain and Northern Ireland')
WHERE don_lib LIKE '%UK%' AND xxx_id IN (SELECT sch_lieu FROM t_souche);