DROP TABLE IF EXISTS clients_de_brclims;

SELECT clt_code, cor_email, cor_libelle, clt_fact_raison_sociale, 
clt_fact_adresse_1, clt_fact_adresse_2, clt_fact_adresse_3, 
clt_fact_code_postal, clt_fact_arrondissement, 
REGEXP_REPLACE(clt_fact_ville, ' (CEDEX|cedex|Cedex)', '') AS ville,
don_lib
INTO clients_de_brclims
FROM t_client
JOIN t_correspondant
ON cor_clt_id = t_client.xxx_id
JOIN t_donneedico
ON clt_fact_pays = t_donneedico.xxx_id
WHERE clt_code NOT SIMILAR TO '10000%'
ORDER BY clt_code;
