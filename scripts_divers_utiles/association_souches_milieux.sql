SELECT t_souche.sch_identifiant, mil_designation_en FROM t_milieu_souche 
JOIN t_souche ON msc_sch_id = t_souche.xxx_id 
JOIN t_milieu ON msc_mil_id = t_milieu.xxx_id;