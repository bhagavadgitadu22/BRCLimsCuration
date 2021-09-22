DROP TABLE IF EXISTS pays_perdu_dans_lieu;

-- on récupère les lieux où un pays est présent
SELECT a.xxx_id, don_lib, (array_agg(a.name_en))[1] AS pays

INTO TEMPORARY TABLE pays_perdu_dans_lieu

FROM (SELECT xxx_id, don_lib, name_en
FROM t_donneedico
JOIN world
ON don_lib LIKE CONCAT('%', name_en, '%')
WHERE don_dic_id IN (3758)
AND don_lib != name_en
AND don_lib NOT SIMILAR TO CONCAT('%', name_en, '[a-zA-Z]%')
AND don_lib NOT SIMILAR TO CONCAT('%[a-zA-Z]', name_en, '%')) AS a

GROUP BY a.xxx_id, don_lib
HAVING COUNT(*) = 1;

-- on fait la jointure avec t_souche en fonction de xxx_id
-- puis on ajoute à précision l'ancienne valeur suivie de " ; " et de la nouvelle valeur
-- on montre les précisions modifiées ensuite
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN REPLACE(don_lib, pays, '')
		ELSE CONCAT(sch_lieu_precis, ' ; '::text, REPLACE(don_lib, pays, ''))
	END
FROM pays_perdu_dans_lieu
WHERE t_souche.sch_lieu = pays_perdu_dans_lieu.xxx_id
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

-- update la valeur dans les lieux directement ensuite
UPDATE t_donneedico
SET don_lib = pays
FROM pays_perdu_dans_lieu
WHERE t_donneedico.xxx_id = pays_perdu_dans_lieu.xxx_id;

-- on drope la temporary table
DROP TABLE IF EXISTS pays_perdu_dans_lieu;
