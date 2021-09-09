-- on vire les lieux de la forme United States of America/WI
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Wisconsin'
		ELSE CONCAT(sch_lieu_precis, ' ; Wisconsin'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib = 'United States of America/WI'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'United States of America'
WHERE don_lib = 'United States of America/WI'
AND don_dic_id IN (3758);


-- on vire les dérivés de Paris
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Saint-Joseph Hospital, Paris'
		ELSE CONCAT(sch_lieu_precis, ' ; Saint-Joseph Hospital, Paris'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib = 'Paris joseph'
AND don_dic_id IN (3758);

UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Pitié-Salpêtrière Hospital, Paris'
		ELSE CONCAT(sch_lieu_precis, ' ; Pitié-Salpêtrière Hospital, Paris'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib = 'Paris pitie'
AND don_dic_id IN (3758);

UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Necker Hospital, Paris'
		ELSE CONCAT(sch_lieu_precis, ' ; Necker Hospital, Paris'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib = 'Hôpital Necker'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'France'
WHERE don_lib IN ('Paris joseph', 'Paris pitie', 'Paris, necker', 'Paris beaujon(clichy)')
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Paris, France'
WHERE don_lib IN ('Paris,France', 'Paris ,France')
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Versailles, France'
WHERE don_lib IN ('Versailles, Paris')
AND don_dic_id IN (3758);


-- mycetoma
-- indiquer le mycetoma dans lieu_precis des souches
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Mycetoma'
		ELSE CONCAT(sch_lieu_precis, ' ; Mycetoma'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib IN ('mycetoma', 'MYCETOMA', 'mycetoma (Alger, Algeria)',
'mycetoma (Dakar, Senegal)', 'mycetoma (Fort-Lamy, Chad)', 'mycetoma (Tunis, Tunisia)', 'mycetoma, (Albania)',
'mycetoma, (Alger, Algeria)', 'MYCETOMA, (Beyrouth)', 'mycetoma, (Cameroon)', 'mycetoma, (Dakar, Senegal)',
'mycetoma, (Dakar, Senegal, 195', 'mycetoma, (Fort-Lamy, Chad)', 'mycetoma, (Maracaibo, Vénézuel', 'MYCETOMA, (Mexico)',
'mycetoma, (Nancy, France)', 'MYCETOMA, (Tunis)', 'MYCETOMA, (Uganda)', 'MYCETOMA,(Djibouti)',
'mycetoma,(Fort-Lamy, Chad)', 'MYCETOMA,(Mexico)', 'MYCETOMA,(Mogadiscio)', 'mycetoma,(Morocco)',
'mycetoma, (Dakar, Senegal, 195', 'mycetoma, (Maracaibo, Vénézuel')
AND don_dic_id IN (3758);

UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Mycetoma of arm'
		ELSE CONCAT(sch_lieu_precis, ' ; Mycetoma of arm'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib IN ('mycetoma of arm')
AND don_dic_id IN (3758);

UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN 'Mycetoma of foot'
		ELSE CONCAT(sch_lieu_precis, ' ; Mycetoma of foot'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib IN ('MYCETOMA OF FOOT, (Cameroon)', 'MYCETOMA OF FOOT,(Uganda)')
AND don_dic_id IN (3758);

-- on met null pour les souches où il y avait juste mycetoma comme lieu
-- puis on supprime ces lieux du dico
UPDATE t_souche
SET sch_lieu = NULL
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib IN ('mycetoma', 'MYCETOMA', 'mycetoma of arm')
AND don_dic_id IN (3758);

DELETE FROM t_donneedico
WHERE don_lib IN ('mycetoma', 'MYCETOMA', 'mycetoma of arm')
AND don_dic_id IN (3758);

-- on met les bons lieux à la place de mycetoma dans le dico
UPDATE t_donneedico
SET don_lib = (SELECT a.matches[1] FROM
(SELECT REGEXP_MATCHES(don_lib, '\(([^)]*)\)') matches) a)
WHERE don_lib IN ('mycetoma (Alger, Algeria)',
'mycetoma (Dakar, Senegal)', 'mycetoma (Fort-Lamy, Chad)', 'mycetoma (Tunis, Tunisia)', 'mycetoma, (Albania)',
'mycetoma, (Alger, Algeria)', 'MYCETOMA, (Beyrouth)', 'mycetoma, (Cameroon)', 'mycetoma, (Dakar, Senegal)', 
'mycetoma, (Fort-Lamy, Chad)', 'MYCETOMA, (Mexico)',
'mycetoma, (Nancy, France)', 'MYCETOMA, (Tunis)', 'MYCETOMA, (Uganda)', 'MYCETOMA,(Djibouti)',
'mycetoma,(Fort-Lamy, Chad)', 'MYCETOMA,(Mexico)', 'MYCETOMA,(Mogadiscio)', 'mycetoma,(Morocco)',
'MYCETOMA OF FOOT, (Cameroon)', 'MYCETOMA OF FOOT,(Uganda)')
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Dakar, Senegal'
WHERE don_lib IN ('mycetoma, (Dakar, Senegal, 195')
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Maracaibo, Venezuela (Bolivarian Republic of)'
WHERE don_lib IN ('mycetoma, (Maracaibo, Vénézuel')
AND don_dic_id IN (3758);


-- on gère les tsukamura
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN CONCAT(TRIM(split_part(don_lib, '(', 1)), ', Japan'::text)
		ELSE CONCAT(sch_lieu_precis, ' ; '::text, TRIM(split_part(don_lib, '(', 1)), ', Japan'::text)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib LIKE '%Tsukamura%'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Japan'
WHERE don_lib LIKE '%Tsukamura%'
AND don_dic_id IN (3758);


-- on gère Scotland, England et Autres
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN don_lib
		ELSE CONCAT(sch_lieu_precis, ' ; '::text, don_lib)
	END
FROM t_donneedico
WHERE t_souche.sch_lieu = t_donneedico.xxx_id
AND don_lib SIMILAR TO '%(Scotland|England)%'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'United Kingdom of Great Britain and Northern Ireland'
WHERE don_lib SIMILAR TO '%(Scotland|England)%'
AND don_dic_id IN (3758);
