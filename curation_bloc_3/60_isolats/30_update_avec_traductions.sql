SELECT sch_isole_a_partir_de, new_isolat
FROM t_souche
JOIN isole_a_partir_de_traduits
ON t_souche.xxx_id = isole_a_partir_de_traduits.xxx_id;

UPDATE t_souche
SET sch_isole_a_partir_de = new_isolat
FROM isole_a_partir_de_traduits
WHERE t_souche.xxx_id = isole_a_partir_de_traduits.xxx_id;
