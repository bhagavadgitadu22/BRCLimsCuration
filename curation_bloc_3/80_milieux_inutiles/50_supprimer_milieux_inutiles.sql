DROP TABLE IF EXISTS milieux_a_ignorer;

-- milieux qu'on ne supprime pas car en fait il y a souches liées contrairement à ce qui était prévu
SELECT t_milieu.xxx_id AS milieu_id, mil_numero, mil_designation_fr, mil_designation_en, t_souche.xxx_id AS souche_id, sch_identifiant, sch_version
INTO milieux_a_ignorer 
FROM t_milieu_souche
JOIN t_milieu 
ON msc_mil_id = t_milieu.xxx_id
JOIN t_souche
ON msc_sch_id = t_souche.xxx_id
WHERE msc_mil_id IN (SELECT id_numero FROM milieux_vides)
ORDER BY mil_numero;

UPDATE t_milieu 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (SELECT id_numero FROM milieux_vides)
AND xxx_id NOT IN (SELECT milieu_id FROM milieux_a_ignorer);

UPDATE t_milieu 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (SELECT id_numero FROM milieux_non_vides);
