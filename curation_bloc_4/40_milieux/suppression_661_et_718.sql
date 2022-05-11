SELECT t_milieu.xxx_id, msc_mil_id, mil_designation_en, sch_identifiant, sch_version, t_milieu.xxx_sup_dat
FROM t_milieu
LEFT JOIN t_milieu_souche
ON msc_mil_id = t_milieu.xxx_id
LEFT JOIN t_souche
ON t_souche.xxx_id = msc_sch_id
WHERE mil_numero = '718'
OR mil_numero = '751A'
OR mil_numero = '661';
--OR mil_numero = '13';

-- de 661 à 13
UPDATE t_milieu_souche
SET msc_mil_id = 1024411
WHERE msc_mil_id = 1028983
AND (msc_sch_id, 1024411) NOT IN (SELECT msc_sch_id, msc_mil_id FROM t_milieu_souche);

DELETE FROM t_milieu_souche
WHERE msc_mil_id = 1028983;

-- de 718 à 751A
UPDATE t_milieu_souche
SET msc_mil_id = 6978809
WHERE msc_mil_id = 1029507
AND (msc_sch_id, 6978809) NOT IN (SELECT msc_sch_id, msc_mil_id FROM t_milieu_souche);

DELETE FROM t_milieu_souche
WHERE msc_mil_id = 1029507;

UPDATE t_milieu 
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (1029507, 1028983);
