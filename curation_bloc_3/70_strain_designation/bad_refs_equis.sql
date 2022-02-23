DROP TABLE IF EXISTS bilan_collections;
DROP TABLE IF EXISTS good_refs;

SELECT t_deposant.don_lib AS collection
INTO bilan_collections
FROM t_souche
JOIN t_donneedico AS t_deposant
ON sch_depositaire = t_deposant.xxx_id
JOIN t_donneedico AS t_categorie
ON t_deposant.don_parent = t_categorie.don_code
AND t_deposant.don_dic_id = t_categorie.don_dic_id
WHERE t_categorie.don_lib = 'Collections'
GROUP BY t_deposant.don_lib
ORDER BY t_deposant.don_lib;

SELECT ref_equi 
INTO good_refs
FROM (SELECT unnest(string_to_array(sch_references_equi, ';')) AS ref_equi
FROM t_souche) AS a
WHERE ref_equi LIKE ANY(SELECT CONCAT(collection, '%') FROM bilan_collections)
OR ref_equi SIMILAR TO '(DSM|WDCM|CPC|CIP|LMG|CARE|CRBIP|KCCM|NBIMCC|NBRL|NCIB)%';

SELECT ref_equi, COUNT(*)
FROM (SELECT unnest(string_to_array(sch_references_equi, ';')) AS ref_equi
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)) AS a
WHERE ref_equi NOT IN (SELECT * FROM good_refs)
GROUP BY ref_equi 
ORDER BY ref_equi;
