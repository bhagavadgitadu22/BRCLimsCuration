DROP TABLE IF EXISTS patho_a_remplir;
DROP TABLE IF EXISTS condensed_patho_a_remplir;

SELECT a.xxx_id, sch_identifiant, sch_version, sch_denomination, taxoshort, sch_pto_id, classe
INTO TABLE patho_a_remplir
FROM (SELECT * FROM last_version_souches_cip) AS a
JOIN (SELECT * FROM pathos_ue WHERE souscat IS NULL) AS b
ON LOWER(sch_denomination) SIMILAR TO CONCAT('%', taxoshort, '%');

SELECT DISTINCT ON (xxx_id) xxx_id, sch_identifiant, sch_version, sch_denomination, taxoshort, sch_pto_id, classe
INTO TABLE condensed_patho_a_remplir
FROM patho_a_remplir
ORDER BY xxx_id, -length(taxoshort);

-- mise a jour de lignes sans patho
SELECT t_souche.sch_identifiant, t_souche.sch_version, t_souche.sch_denomination, 
(SELECT pto_lib FROM t_pathogenicite WHERE xxx_id = t_souche.sch_pto_id), (SELECT pto_lib FROM t_pathogenicite WHERE pto_lib = classe)
FROM t_souche
JOIN condensed_patho_a_remplir
ON t_souche.xxx_id = condensed_patho_a_remplir.xxx_id
WHERE t_souche.sch_pto_id IS NULL
ORDER BY classe DESC;

-- mise a jour de lignes ou il y avait deja une patho
SELECT t_souche.sch_identifiant, t_souche.sch_version, t_souche.sch_denomination, 
(SELECT pto_lib FROM t_pathogenicite WHERE xxx_id = t_souche.sch_pto_id), (SELECT pto_lib FROM t_pathogenicite WHERE pto_lib = classe)
FROM t_souche
JOIN condensed_patho_a_remplir
ON t_souche.xxx_id = condensed_patho_a_remplir.xxx_id
WHERE t_souche.sch_pto_id != (SELECT xxx_id FROM t_pathogenicite WHERE pto_lib = classe)
ORDER BY classe DESC;

UPDATE t_souche
SET sch_pto_id = (SELECT xxx_id FROM t_pathogenicite WHERE pto_lib = classe)
FROM condensed_patho_a_remplir
WHERE t_souche.xxx_id = condensed_patho_a_remplir.xxx_id;
AND (t_souche.sch_pto_id IS NULL OR t_souche.sch_pto_id != (SELECT xxx_id FROM t_pathogenicite WHERE pto_lib = classe));
