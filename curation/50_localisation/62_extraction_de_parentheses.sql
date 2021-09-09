DROP TABLE IF EXISTS pays_entre_parentheses;

-- on recupere la liste des pays contenus dans ()
SELECT xxx_id, don_lib, content, REPLACE(don_lib, CONCAT('(', content, ')'), '') AS replacement

INTO TEMPORARY TABLE pays_entre_parentheses

FROM (SELECT xxx_id, don_lib, (REGEXP_MATCHES(don_lib, '\(([^)]*)\)'))[1] AS content
FROM t_donneedico
WHERE don_lib SIMILAR TO '%\([^)]*\)%'
AND don_dic_id IN (3758)) AS a
WHERE content IN (SELECT name_en FROM world);

-- on fait la jointure avec t_souche en fonction de xxx_id
-- puis on ajoute à précision l'ancienne valeur suivie de " ; " et de la nouvelle valeur
-- on montre les précisions modifiées ensuite
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN replacement
		ELSE CONCAT(sch_lieu_precis, ' ; '::text, replacement)
	END
FROM pays_entre_parentheses
WHERE t_souche.sch_lieu = pays_entre_parentheses.xxx_id;

-- update la valeur dans les lieux directement ensuite
UPDATE t_donneedico
SET don_lib = content
FROM pays_entre_parentheses
WHERE t_donneedico.xxx_id = pays_entre_parentheses.xxx_id;

-- on drope la temporary table
DROP TABLE IF EXISTS pays_entre_parentheses;
