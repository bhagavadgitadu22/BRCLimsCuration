DROP TABLE IF EXISTS souches_chryseos;

CREATE TABLE souches_chryseos (
	souche text
);

COPY souches_chryseos (souche)
FROM '/mnt/gaia/my_home/chryseobacterium2/29_liste_souches_etudies.csv'
DELIMITER '|';
