UPDATE t_souche
SET sch_taxonomie = (SELECT species.xxx_id 
					 FROM t_donneedico as species
					 JOIN t_donneedico as genus
					 ON genus.don_code = species.don_parent
					 WHERE species.don_dic_id = 3755 AND genus.don_dic_id = 3755
					 AND species.don_lib = 'svalbardensis' AND genus.don_lib = 'Arcticibacter')
WHERE sch_identifiant = 'CIP 110422T';

UPDATE t_souche
SET sch_taxonomie = (SELECT species.xxx_id 
					 FROM t_donneedico as species
					 JOIN t_donneedico as genus
					 ON genus.don_code = species.don_parent
					 WHERE species.don_dic_id = 3755 AND genus.don_dic_id = 3755
					 AND species.don_lib = 'aurum' AND genus.don_lib = 'Mycolicibacterium')
WHERE sch_identifiant = 'CIP 105688';

UPDATE t_souche
SET sch_taxonomie = (SELECT species.xxx_id 
					 FROM t_donneedico as species
					 JOIN t_donneedico as genus
					 ON genus.don_code = species.don_parent
					 WHERE species.don_dic_id = 3755 AND genus.don_dic_id = 3755
					 AND species.don_lib = 'hirudinis' AND genus.don_lib = 'Niabella')
WHERE sch_identifiant = 'CIP 110416T';

UPDATE t_souche
SET sch_taxonomie = 27753
WHERE sch_identifiant = 'CIP 203494';

UPDATE t_souche
SET sch_taxonomie = 27829
WHERE sch_identifiant = 'CRBIP3.1863';

UPDATE t_souche
SET sch_taxonomie = 25180
WHERE sch_identifiant = 'CIP 203304';
