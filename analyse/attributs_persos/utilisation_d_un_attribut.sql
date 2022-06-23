SELECT att_filtre, col_descr, COUNT(*), 
array_to_string(ARRAY_AGG(DISTINCT don_lib), ';'), array_to_string(ARRAY_AGG(DISTINCT sch_identifiant), ';') 
FROM t_attribut 
JOIN t_dico_liste_val 
ON dlv_att_id = t_attribut.xxx_id 
JOIN t_souche ON dlv_entite_id = t_souche.xxx_id AND t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
JOIN t_collection 
ON att_col_id = t_collection.xxx_id 
JOIN t_donneedico 
ON dlv_valeur = t_donneedico.xxx_id 
WHERE att_nom = 'Méthode 4' 
GROUP BY col_descr;
