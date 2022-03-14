DROP TABLE IF EXISTS milieux_vides;
DROP TABLE IF EXISTS milieux_non_vides;

CREATE TABLE milieux_vides (
	numero varchar(32),
	id_numero integer
);

CREATE TABLE milieux_non_vides (
	numero varchar(32),
	id_numero integer,
	remplacant varchar(32),
	id_remplacant integer
);
