-- on récupère les ids de lieux dans donnee_dico qui contiennent un nom de ville
SELECT id_lieu, city_ascii, country 
INTO TEMPORARY TABLE ids_lieux_villes

FROM (SELECT t_donneedico.xxx_id AS id_lieu, don_lib
FROM t_donneedico
INNER JOIN t_souche 
ON t_donneedico.xxx_id = t_souche.sch_lieu
GROUP BY t_donneedico.xxx_id) AS lieux

JOIN world_cities
ON lieux.don_lib = world_cities.city_ascii
WHERE world_cities.city_ascii NOT IN (SELECT name_en FROM world) AND world_cities.city_ascii != world_cities.country;

-- on fait la jointure avec t_souche en fonction de xxx_id/id_lieu
-- puis on ajoute à précision l'ancienne valeur suivie de " ; " et de la nouvelle valeur
-- on montre les précisions modifiées ensuite
UPDATE t_souche
SET sch_lieu_precis =
	CASE sch_lieu_precis
		WHEN '' THEN city_ascii
		ELSE CONCAT(sch_lieu_precis, ' ; '::text, city_ascii)
	END
FROM ids_lieux_villes
WHERE t_souche.sch_lieu = ids_lieux_villes.id_lieu;

-- update la valeur dans les lieux directement ensuite
UPDATE t_donneedico AS tdd
SET don_lib = country
FROM ids_lieux_villes
WHERE tdd.xxx_id = ids_lieux_villes.id_lieu;

-- on drope la temporary table
DROP TABLE IF EXISTS ids_lieux_villes;