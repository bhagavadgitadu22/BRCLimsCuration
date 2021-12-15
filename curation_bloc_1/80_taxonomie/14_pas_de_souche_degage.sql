DROP TABLE IF EXISTS souches_sans_souches;

-- on selectionne les taxos avec pas de souche et les souches associées
SELECT t_souche.xxx_id
INTO TEMPORARY TABLE souches_sans_souches
FROM t_donneedico
JOIN t_souche
ON t_donneedico.xxx_id = sch_taxonomie
WHERE don_lib LIKE '%pas de souche%' 
AND sch_denomination NOT LIKE '%pas de souche%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND t_donneedico.xxx_sup_dat IS NULL;

-- on ajoute pas de souche dans la dénomination des souches où ce n'était pas le cas
UPDATE t_souche
SET sch_denomination = CONCAT(sch_denomination, ' pas de souche')
WHERE xxx_id IN (SELECT * FROM souches_sans_souches);

-- on vire les pas de souche
UPDATE t_donneedico
SET don_lib = REPLACE(don_lib, 'pas de souche', '')
WHERE don_dic_id = 3755
AND xxx_sup_dat IS NULL;

DROP TABLE IF EXISTS souches_sans_souches;
