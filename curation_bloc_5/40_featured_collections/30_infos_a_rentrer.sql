/*
SELECT t_souche.xxx_id, panels
/*, (SELECT col_clg_id FROM t_collection WHERE xxx_id = sch_col_id) */
FROM panels_crbip_grouped
JOIN t_souche
ON REPLACE(identifiant, 'CIP1', 'CIP 1') = sch_identifiant;
*/

INSERT INTO t_string_val (svl_entite_id, svl_att_id, svl_valeur)
SELECT t_souche.xxx_id, t_attribut.xxx_id, panels
FROM panels_crbip_grouped
JOIN t_souche
ON REPLACE(identifiant, 'CIP1', 'CIP 1') = sch_identifiant
JOIN t_attribut
ON att_col_id = sch_col_id
AND att_nom = 'Featured collections'
LEFT JOIN t_string_val
ON svl_entite_id = t_souche.xxx_id
AND svl_att_id = t_attribut.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND t_string_val.xxx_id IS NULL
AND t_attribut.xxx_id IS NOT NULL
ORDER BY t_souche.xxx_id;

/*
SELECT t_souche.xxx_id, panels
FROM panels_crbip_grouped
LEFT JOIN t_souche
ON REPLACE(identifiant, 'CIP1', 'CIP 1') = sch_identifiant
WHERE t_souche.xxx_id IS NULL;
*/
