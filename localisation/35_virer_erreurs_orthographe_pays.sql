UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Czech Republic', 'Czechia')
WHERE don_lib LIKE '%Czech Republic%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'The Netherlands', 'Netherlands')
WHERE don_lib LIKE '%The Netherlands%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Burkina', 'Burkina Faso')
WHERE don_lib LIKE '%Burkina%'
AND don_lib NOT LIKE '%Burkina Faso%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Vietnam', 'Viet Nam')
WHERE don_lib LIKE '%Vietnam%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Venezuela', 'Venezuela (Bolivarian Republic of)')
WHERE don_lib LIKE '%Venezuela%'
AND don_lib NOT LIKE '%Venezuela (Bolivarian Republic of)%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Democratic Republic of the Congo', 'Congo, Democratic Republic of the')
WHERE don_lib LIKE '%Democratic Republic of the Congo%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Ivory Coast', 'Côte d''Ivoire')
WHERE don_lib LIKE '%Ivory Coast%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Taiwan', 'Taiwan, Province of China')
WHERE don_lib LIKE '%Taiwan%'
AND don_lib NOT LIKE '%Taiwan, Province of China%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Iran', 'Iran (Islamic Republic of)')
WHERE don_lib LIKE '%Iran%'
AND don_lib NOT LIKE '%Iran (Islamic Republic of)%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Russia', 'Russian Federation')
WHERE don_lib LIKE '%Russia%'
AND don_lib NOT LIKE '%Russian Federation%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);
