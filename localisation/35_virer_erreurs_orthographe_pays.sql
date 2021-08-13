UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Czech Republic', 'Czechia')
WHERE don_lib LIKE '%Czech Republic%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Czechiah', 'Czechia')
WHERE don_lib LIKE '%Czechiah%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'The Netherlands', 'Netherlands')
WHERE don_lib LIKE '%The Netherlands%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Netherland', 'Netherlands')
WHERE don_lib LIKE '%Netherland%'
AND don_lib NOT LIKE '%Netherlands%'
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
SET don_lib = REPLACE(don_lib, 'Vietnâm', 'Viet Nam')
WHERE don_lib LIKE '%Vietnâm%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Viêtnam', 'Viet Nam')
WHERE don_lib LIKE '%Viêtnam%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Venezuela', 'Venezuela (Bolivarian Republic of)')
WHERE don_lib LIKE '%Venezuela%'
AND don_lib NOT LIKE '%Venezuela (Bolivarian Republic of)%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Democratic Republic of the Congo', 'Congo (Democratic Republic of the)')
WHERE don_lib LIKE '%Democratic Republic of the Congo%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Ivory Coast', 'Côte d''Ivoire')
WHERE don_lib LIKE '%Ivory Coast%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Cote d''Ivoire', 'Côte d''Ivoire')
WHERE don_lib LIKE '%Cote d''Ivoire%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Taiwan', 'Taiwan (Province of China)')
WHERE don_lib LIKE '%Taiwan%'
AND don_lib NOT LIKE '%Taiwan (Province of China)%'
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

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Bolivia', 'Bolivia (Plurinational State of)')
WHERE don_lib LIKE '%Bolivia%'
AND don_lib NOT LIKE '%Bolivia (Plurinational State of)%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Slovak Republic', 'Slovakia')
WHERE don_lib LIKE '%Slovak Republic%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Italia', 'Italy')
WHERE don_lib LIKE '%Italia%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'RCA', 'Central African Republic')
WHERE don_lib = 'RCA'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Tanzania', 'Tanzania (United Republic of)')
WHERE don_lib LIKE 'Tanzania'
AND don_lib NOT LIKE 'Tanzania (United Republic of)'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Koweit', 'Kuwait')
WHERE don_lib LIKE 'Koweit'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Macau', 'Macao')
WHERE don_lib LIKE 'Macau'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Antartica', 'Antarctica')
WHERE don_lib LIKE '%Antartica%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'French Guyana', 'French Guiana')
WHERE don_lib LIKE '%French Guyana%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Zaïre', 'Democratic Republic of the Congo')
WHERE don_lib LIKE '%Zaïre%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Zaire', 'Democratic Republic of the Congo')
WHERE don_lib LIKE '%Zaire%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Syria', 'Syrian Arab Republic')
WHERE don_lib LIKE '%Syria%'
AND don_lib NOT LIKE '%Syrian Arab Republic%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Burma', 'Myanmar')
WHERE don_lib LIKE '%Burma%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Roumania', 'Romania')
WHERE don_lib LIKE '%Roumania%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'South Korea', 'Korea (Republic of)')
WHERE don_lib LIKE '%South Korea%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Republic Central Africa', 'Central African Republic')
WHERE don_lib LIKE '%Republic Central Africa%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Republic of the Philippines', 'Philippines')
WHERE don_lib LIKE '%Republic of the Philippines%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Portgual', 'Portugal')
WHERE don_lib LIKE '%Portgual%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Thaïland', 'Thailand')
WHERE don_lib LIKE '%Thaïland%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Antartic ocean', 'Antarctic ocean')
WHERE don_lib LIKE '%Antartic ocean%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Perou', 'Peru')
WHERE don_lib LIKE '%Perou%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Autralia', 'Australia')
WHERE don_lib LIKE '%Autralia%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);

UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'Geece', 'Greece')
WHERE don_lib LIKE '%Geece%'
AND don_dic_id IN (3758, 4236195, 554373, 54117, 593885);