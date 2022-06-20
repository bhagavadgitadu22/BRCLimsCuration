/*
SELECT sch_identifiant
FROM t_souche
JOIN chemins_taxonomie
ON t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path = 'Clostridium difficile'
AND sch_denomination = 'Clostridioides difficile';
*/

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Clostridioides difficile')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Clostridium difficile'
AND sch_denomination = 'Clostridioides difficile';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Cutibacterium acnes')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Propionibacterium acnes'
AND sch_denomination = 'Cutibacterium acnes';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Cutibacterium acnes acnes')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Propionibacterium acnes'
AND sch_denomination = 'Cutibacterium acnes acnes';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Cutibacterium acnes defendens')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Propionibacterium acnes'
AND sch_denomination = 'Cutibacterium acnes defendens';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Cutibacterium avidum')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Propionibacterium avidum'
AND sch_denomination = 'Cutibacterium avidum';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Enterocloster bolteae')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Clostridium bolteae'
AND sch_denomination = 'Enterocloster bolteae';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Lelliottia amnigena')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Enterobacter amnigenus'
AND sch_denomination = 'Lelliottia amnigena';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Mycolicibacterium smegmatis')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Mycobacterium smegmatis'
AND sch_denomination = 'Mycolicibacterium smegmatis';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Stenotrophomonas maltophilia')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Xanthomonas maltophilia'
AND sch_denomination = 'Stenotrophomonas maltophilia';

UPDATE t_souche
SET sch_taxonomie = (SELECT sch_taxonomie FROM chemins_taxonomie
WHERE path LIKE 'Streptococcus anginosus anginosus')
FROM chemins_taxonomie
WHERE t_souche.sch_taxonomie = chemins_taxonomie.sch_taxonomie
AND xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND path LIKE 'Streptococcus anginosus subsp. anginosus'
AND sch_denomination = 'Streptococcus anginosus anginosus';
