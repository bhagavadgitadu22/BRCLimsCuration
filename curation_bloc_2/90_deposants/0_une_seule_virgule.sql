/*
SELECT t_deposant.xxx_id, t_deposant.don_lib
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
AND (CHAR_LENGTH(t_deposant.don_lib) - CHAR_LENGTH(REPLACE(t_deposant.don_lib, ',', ''))) > 1
ORDER BY t_deposant.xxx_id;
*/

UPDATE t_donneedico
SET don_lib = trim(don_lib, ',')
WHERE don_dic_id = 104
AND don_lib != trim(don_lib, ',');

UPDATE t_donneedico
SET don_lib = 'S. Nakamura, RICMB Osaka'
WHERE don_dic_id = 104
AND don_lib = 'S. Nakamura, RICMB, Osaka';

UPDATE t_donneedico
SET don_lib = 'Y. Fleury, LBCM Southern Brittany University'
WHERE don_dic_id = 104
AND don_lib = 'Y. Fleury, LBCM, Univ. Bretagne';

UPDATE t_donneedico
SET don_lib = 'P.Bergsten, Matis Iceland'
WHERE don_dic_id = 104
AND don_lib = 'P.Bergsten, Matis, Iceland';

UPDATE t_donneedico
SET don_lib = 'K. Jalava, Faculty of Veterinary Medicine of Helsinki University'
WHERE don_dic_id = 104
AND don_lib = 'K. Jalava, Faculty of Veterinay Medicine, Helsinki University';

UPDATE t_donneedico
SET don_lib = 'J. Bador and C. Neuwirth and L. Amoureux, Dijon Hospital'
WHERE don_dic_id = 104
AND don_lib = 'J. Bador, C. Neuwirth, L. Amoureux, Dijon Hospital';

UPDATE t_donneedico
SET don_lib = 'R. Harasawa, Animal Center Biomedical Research of the Faculty of Medicine of Tokyo University'
WHERE don_dic_id = 104
AND don_lib = 'R. Harasawa, Animal Center Biomedical Research, Faculty of Medicine, Tokyo University';

UPDATE t_donneedico
SET don_lib = CONCAT('K. Rose, IMMB Westf', CHR(132), 'lische Wilhelms Münster University')
WHERE don_dic_id = 104
AND don_lib = CONCAT('K. Rose, IMMB Westf', CHR(132), 'lische Wilhelms Münster University');

UPDATE t_donneedico
SET don_lib = 'G. Reuter, Institute for Food Hygiene of Berlin-Dahlem Free University'
WHERE don_dic_id = 104
AND don_lib = 'G. Reuter, Institute for Food Hygiene, Berlin-Dahlem Free University';

UPDATE t_donneedico
SET don_lib = CONCAT('K. Tr', CHR(129), 'lzsch, Max von Pettenkofer Institute of Munich University')
WHERE don_dic_id = 104
AND don_lib = CONCAT('K. Tr', CHR(129), 'lzsch, Max von Pettenkofer Institute of Munich University');

UPDATE t_donneedico
SET don_lib = CONCAT('A. Steinb', CHR(129), 'chel, Munster (Germany)')
WHERE don_dic_id = 104
AND don_lib = CONCAT('A. Steinb', CHR(129), 'chel, Munster, Germany');
