DROP TABLE IF EXISTS infos_care;

CREATE TABLE infos_care (
	numero serial,
	sch_denomination text, 
	sch_taxonomie integer, 
	sch_proprietes text, 
	sch_origine integer, 
	sch_pto_id integer, 
	sch_isole_a_partir_de text, 
	sch_lieu integer, 
	sch_dat_prelevement text, 
	sch_bibliographie text, 
	sch_temperature_incubation text, 
	sch_historique text, 
	sch_depositaire integer
);
