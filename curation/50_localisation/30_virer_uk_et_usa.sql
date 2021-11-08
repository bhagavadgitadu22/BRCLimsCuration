-- pour usa
UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'U.S.A.', 'United States of America')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%U.S.A.%' 
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'USA.', 'United States of America')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%USA.%' 
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'USA', 'United States of America')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%USA%' 
AND don_lib NOT SIMILAR TO CONCAT('%USA[a-zA-Z]%')
AND don_lib NOT SIMILAR TO CONCAT('%[a-zA-Z]USA%')
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'U.S.A', 'United States of America')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%U.S.A%' 
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'United States', 'United States of America')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%United States%' 
AND don_lib NOT LIKE '%United States of America%' 
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

-- pour uk
UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'U.K.', 'United Kingdom of Great Britain and Northern Ireland')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%U.K.%' 
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'UK', 'United Kingdom of Great Britain and Northern Ireland')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%UK%' 
AND don_lib NOT SIMILAR TO CONCAT('%UK[a-zA-Z]%')
AND don_lib NOT SIMILAR TO CONCAT('%[a-zA-Z]UK%')
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Uk', 'United Kingdom of Great Britain and Northern Ireland')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%Uk%' 
AND don_lib NOT SIMILAR TO CONCAT('%Uk[a-zA-Z]%')
AND don_lib NOT SIMILAR TO CONCAT('%[a-zA-Z]Uk%')
AND xxx_id IN (SELECT sch_lieu FROM t_souche);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'United Kingdom', 'United Kingdom of Great Britain and Northern Ireland')
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%United Kingdom%' 
AND don_lib NOT LIKE '%United Kingdom of Great Britain and Northern Ireland%'
AND xxx_id IN (SELECT sch_lieu FROM t_souche);