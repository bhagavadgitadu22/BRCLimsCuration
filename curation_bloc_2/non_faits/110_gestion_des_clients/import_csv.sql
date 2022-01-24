DROP TABLE IF EXISTS excel_de_clients;

CREATE TABLE excel_de_clients (
	code varchar(100),
	civilite varchar(100),
	nom varchar(100),
	nom2 varchar(100),
	adresse varchar(100),
	adresse2 varchar(100),
	code_postal varchar(100),
	ville varchar(100),
	pays varchar(100),
	boite_postale varchar(100),
	zone varchar(100),
	tva varchar(100),
	siret varchar(100),
	siren varchar(100),
	groupe1 varchar(100),
	groupe2 varchar(100),
	fonds varchar(100),
	tva2 varchar(100)
);

COPY excel_de_clients (code, civilite, nom, nom2, adresse, adresse2, code_postal,
	ville, pays, boite_postale, zone, tva, siret, siren,
	groupe1, groupe2, fonds, tva2)
FROM 'C:/Users/Public/Documents/clients_brclims.csv'
DELIMITER ';';
