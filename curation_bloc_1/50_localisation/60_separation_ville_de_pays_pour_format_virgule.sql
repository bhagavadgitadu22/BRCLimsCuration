DROP TABLE IF EXISTS pays_au_format_virgule;

-- on récupère la liste des lieux dans t_donneedico du type "blabla, pays" en séparant le blabla du pays
SELECT xxx_id, beginning_str, end_str 

INTO TEMPORARY TABLE pays_au_format_virgule

FROM (SELECT xxx_id,
TRIM(substring(don_lib, '^(.*),')) AS beginning_str,
TRIM(substring(don_lib, '[^,]*$')) AS end_str
FROM t_donneedico 
WHERE don_dic_id IN (3758)
AND xxx_sup_dat IS NULL
AND don_lib LIKE '%, %'
GROUP BY xxx_id) AS separationvirgule

INNER JOIN world
ON separationvirgule.end_str = world.name_en;

-- on fait la jointure avec t_souche en fonction de xxx_id
-- puis on ajoute à précision l'ancienne valeur suivie de " ; " et de la nouvelle valeur
-- on montre les précisions modifiées ensuite
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN beginning_str
		ELSE CONCAT(sch_lieu_precis, ' ; '::text, beginning_str)
	END
FROM pays_au_format_virgule
WHERE t_souche.sch_lieu = pays_au_format_virgule.xxx_id
AND t_souche.xxx_sup_dat IS NULL;

-- update la valeur dans les lieux directement ensuite
UPDATE t_donneedico AS tdd
SET don_lib = end_str
FROM pays_au_format_virgule
WHERE tdd.xxx_id = pays_au_format_virgule.xxx_id;

-- on drope la temporary table
DROP TABLE IF EXISTS pays_au_format_virgule;
