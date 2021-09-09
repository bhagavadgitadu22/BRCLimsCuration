UPDATE t_souche
SET sch_lieu_precis = 'Vestfold Hills'
WHERE xxx_id = 83763
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_donneedico
SET don_lib = 'Antarctica'
WHERE don_lib = 'Antarctic coast'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Off the West African coast, Atlantic Ocean'
WHERE don_lib = 'Coast, West Africa'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'East Pacific Rise, Pacific Ocean'
WHERE don_lib = 'East Pacific'
OR don_lib = 'East Pacific rise'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Northwest Pacific, Pacific Ocean'
WHERE don_lib = 'Northwest Pacific'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Shallow coastal region of Keel, Taiwan (Province of China)'
WHERE don_lib = 'Shallow coastal region of Keel'
AND don_dic_id IN (3758);

UPDATE t_souche
SET sch_lieu_precis = '',
	sch_lieu = (SELECT xxx_id FROM t_donneedico WHERE don_lib = 'Central African Republic')
FROM t_donneedico
WHERE sch_lieu = t_donneedico.xxx_id
AND sch_lieu_precis LIKE '%Centrafrican Republic%'
AND t_donneedico.don_lib = 'Africa'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'JPF, France'
WHERE don_lib = 'JPF'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Alboran Sea, Mediterranean Sea'
WHERE don_lib = 'Alboran sea'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Shore, Adriatic Sea'
WHERE don_lib = 'Adriatic shore'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Human vagina, France'
WHERE don_lib = 'Human, vagina'
AND don_dic_id IN (3758);
