SELECT t_souche.xxx_id, panels
/*, (SELECT col_clg_id FROM t_collection WHERE xxx_id = sch_col_id) */
FROM panels_crbip_grouped
JOIN t_souche
ON REPLACE(identifiant, 'CIP1', 'CIP 1') = sch_identifiant;

/*
supprimer ancien attribut perso Featured Collections rendu inutile
*/

/*
SELECT t_souche.xxx_id, panels
FROM panels_crbip_grouped
LEFT JOIN t_souche
ON REPLACE(identifiant, 'CIP1', 'CIP 1') = sch_identifiant
WHERE t_souche.xxx_id IS NULL;
*/
