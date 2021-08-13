DROP TABLE IF EXISTS lieux_avec_dates;
DROP TABLE IF EXISTS lieu_egal_annee;

-- on récupère les souches où une date était indiquée
SELECT t_donneedico.xxx_id, don_lib,
(REGEXP_MATCHES(don_lib, ', (([0-9]+\/[0-9]+\/[0-9]+)|([0-9]+\/[0-9]+)|([0-9]{4}))'))[1] AS date_non_formatted
INTO TEMPORARY TABLE lieux_avec_dates
FROM t_donneedico
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND don_lib SIMILAR TO '%, (([0-9]+\/[0-9]+\/[0-9]+)|([0-9]+\/[0-9]+)|([0-9]{4}))%';

ALTER TABLE lieux_avec_dates ADD COLUMN date_formatted timestamp without time zone;

UPDATE lieux_avec_dates
SET date_formatted = TO_TIMESTAMP(date_non_formatted, 'DD/MM/YYYY')
WHERE date_non_formatted SIMILAR TO '%[0-9]+\/[0-9]+\/[0-9]{4}%'
AND date_non_formatted IS NULL;

UPDATE lieux_avec_dates
SET date_formatted = TO_TIMESTAMP(date_non_formatted, 'DD/MM/YY')
WHERE date_non_formatted SIMILAR TO '%[0-9]+\/[0-9]+\/[0-9]{2}%'
AND date_non_formatted IS NULL;

UPDATE lieux_avec_dates
SET date_formatted = TO_TIMESTAMP(date_non_formatted, 'YYYY')
WHERE date_non_formatted SIMILAR TO '%[0-9]{4}%'
AND date_non_formatted IS NULL;

UPDATE lieux_avec_dates
SET date_formatted = TO_TIMESTAMP(date_non_formatted, 'MM/YY')
WHERE date_non_formatted SIMILAR TO '%[0-9]+\/[0-9]+%'
AND date_non_formatted IS NULL;

-- on fait la jointure avec t_souche en fonction de xxx_id
-- puis on met comme date la date récupérée
UPDATE t_souche
SET sch_dat_acquisition = date_formatted
FROM lieux_avec_dates
WHERE t_souche.sch_lieu = lieux_avec_dates.xxx_id;

-- update la valeur dans les lieux directement ensuite
UPDATE t_donneedico
SET don_lib = REPLACE(lieux_avec_dates.don_lib, CONCAT(', ', date_non_formatted), '')
FROM lieux_avec_dates
WHERE t_donneedico.xxx_id = lieux_avec_dates.xxx_id;


-- on récupère les souches où la localisation était juste une année
SELECT xxx_id, don_lib
INTO TEMPORARY TABLE lieu_egal_annee
FROM t_donneedico
WHERE don_dic_id IN (3758, 4236195, 554373, 54117, 593885)
AND don_lib SIMILAR TO '[0-9]{4}';

-- on fait la jointure avec t_souche en fonction de xxx_id
-- puis on met comme date la date récupérée
UPDATE t_souche
SET sch_dat_acquisition = TO_TIMESTAMP(don_lib, 'YYYY'),
	sch_lieu = NULL
FROM lieu_egal_annee
WHERE t_souche.sch_lieu = lieu_egal_annee.xxx_id;

-- update la valeur dans les lieux directement ensuite
DELETE FROM t_donneedico
WHERE xxx_id IN (SELECT xxx_id FROM lieu_egal_annee);

DROP TABLE IF EXISTS lieux_avec_dates;
DROP TABLE IF EXISTS lieu_egal_annee;
