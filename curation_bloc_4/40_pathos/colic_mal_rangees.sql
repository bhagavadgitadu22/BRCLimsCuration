--simple
SELECT t_souche .xxx_id, sch_identifiant, sch_version, sch_denomination, pto_lib, sch_proprietes
FROM t_souche 
LEFT JOIN t_pathogenicite
ON t_pathogenicite.xxx_id = sch_pto_id
WHERE sch_denomination LIKE 'Escherichia coli%' 
AND sch_proprietes SIMILAR TO '%(EHEC|UPEC|EPEC|ETEC|STEC|ECEH|ECEI|ECEP|ECET)%'
AND pto_lib != '3';

--complexe inutilement
SELECT t_souche .xxx_id, sch_identifiant, sch_version, sch_denomination, 
pto_lib, sch_proprietes, t_cpc.svl_valeur, t_strain_designation.svl_valeur
FROM t_souche 

LEFT JOIN t_pathogenicite
ON t_pathogenicite.xxx_id = sch_pto_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Code produit collection') AS t_cpc
ON t_cpc.att_col_id = t_souche.sch_col_id
AND t_cpc.svl_entite_id = t_souche.xxx_id
LEFT JOIN (SELECT att_col_id, svl_entite_id, svl_valeur FROM t_attribut 
		   LEFT JOIN t_string_val ON t_string_val.svl_att_id = t_attribut.xxx_id
		   WHERE att_nom = 'Strain Designation') AS t_strain_designation
ON t_strain_designation.att_col_id = t_souche.sch_col_id
AND t_strain_designation.svl_entite_id = t_souche.xxx_id

WHERE sch_denomination LIKE 'Escherichia coli%' 
AND (sch_proprietes SIMILAR TO '%(EHEC|UPEC|EPEC|ETEC|STEC|ECEH|ECEI|ECEP|ECET)%'
	 OR sch_historique SIMILAR TO '%(EHEC|UPEC|EPEC|ETEC|STEC|ECEH|ECEI|ECEP|ECET)%'
	 OR t_cpc.svl_valeur SIMILAR TO '%(EHEC|UPEC|EPEC|ETEC|STEC|ECEH|ECEI|ECEP|ECET)%'
	 OR t_strain_designation.svl_valeur SIMILAR TO '%(EHEC|UPEC|EPEC|ETEC|STEC|ECEH|ECEI|ECEP|ECET)%')
AND pto_lib != '3';
