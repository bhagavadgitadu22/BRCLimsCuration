-- elements dont je ne tiens pas compte car moins precis que d'autres
-- exemple info sur helicobacter pylory a priorite sur infos sur tous les helicobacter en general
SELECT *
FROM patho_a_remplir
JOIN condensed_patho_a_remplir
ON patho_a_remplir.xxx_id = condensed_patho_a_remplir.xxx_id
AND patho_a_remplir.taxoshort != condensed_patho_a_remplir.taxoshort;

-- redondances dans bdd avec même taxo mais patho différente
SELECT *
FROM pathos_ue AS p1
JOIN pathos_ue AS p2
ON p1.classe != p2.classe
AND p1.taxoshort = p2.taxoshort
AND p1.souscat IS NULL AND p2.souscat IS NULL;

-- espèces que je n'ai pas géré
SELECT *
FROM pathos_ue
LEFT JOIN patho_a_remplir
ON pathos_ue.taxoshort = patho_a_remplir.taxoshort
WHERE patho_a_remplir.taxoshort IS NULL
AND pathos_ue.souscat IS NULL;

-- Shigella dysenteriae à 3 ok
SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, pto_lib
FROM t_souche
JOIN t_pathogenicite
ON sch_pto_id = t_pathogenicite.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_denomination = 'Shigella dysenteriae 1';

-- Salmonella Typhi à 3 ok
SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, pto_lib
FROM t_souche
JOIN t_pathogenicite
ON sch_pto_id = t_pathogenicite.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_denomination LIKE 'Salmonella%'
AND (LOWER(sch_denomination) LIKE '% typhi %'
OR LOWER(sch_denomination) LIKE '% typhi');
