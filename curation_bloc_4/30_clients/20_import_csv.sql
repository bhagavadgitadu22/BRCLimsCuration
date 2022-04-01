COPY avec_sap (sap, nom, mail)
FROM 'C:/Users/Public/Documents/mails_avec_sap_utf.csv'
DELIMITER ';' CSV HEADER;

COPY sans_sap (nom, pays, mail)
FROM 'C:/Users/Public/Documents/mails_sans_sap_utf.csv'
DELIMITER ';' CSV HEADER;
