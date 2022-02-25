SELECT t_souche.xxx_id, sch_identifiant, sch_version, sch_denomination, t_lot.xxx_id, col_nom, svl_valeur AS cpc
FROM t_souche
LEFT JOIN t_collection
ON sch_col_id = t_collection.xxx_id
LEFT JOIN t_lot
ON lot_sch_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Code produit collection') AS t_cpc
ON t_cpc.att_col_id = t_souche.sch_col_id
AND t_cpc.svl_entite_id = t_souche.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND t_lot.xxx_id IS NULL
AND LOWER(sch_denomination) SIMILAR TO '%(unnamed|unidentified)%'
ORDER BY sch_identifiant;
