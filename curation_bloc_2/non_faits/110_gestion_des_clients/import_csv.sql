DROP TABLE IF EXISTS excel_de_clients;

CREATE TABLE excel_de_clients (
	code integer,
	civilite varchar(100),
	nom varchar(100),
	nom2 varchar(100),
	adresse varchar(100),
	code_postal varchar(100),
	siret varchar(100),
	siren varchar(100),
	groupe1 varchar(100),
	groupe2 varchar(100),
	groupe3 varchar(100),
	ending varchar(100)
);

COPY excel_de_clients (code, civilite, nom, nom2, adresse, code_postal, 
					siret, siren, groupe1, groupe2, groupe3, ending)
FROM 'C:/Users/Public/Documents/clients_brclims.csv'
DELIMITER ';';
