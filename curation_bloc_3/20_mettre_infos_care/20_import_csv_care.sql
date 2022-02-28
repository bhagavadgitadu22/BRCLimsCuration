COPY infos_care (sch_denomination, sch_taxonomie, sch_proprietes, sch_origine, 
				 sch_pto_id, sch_isole_a_partir_de, sch_lieu, sch_dat_prelevement, 
				 sch_bibliographie, sch_temperature_incubation, sch_historique, sch_depositaire)
FROM 'C:/Users/Public/Documents/infos_care.csv'
DELIMITER '|' CSV HEADER;
