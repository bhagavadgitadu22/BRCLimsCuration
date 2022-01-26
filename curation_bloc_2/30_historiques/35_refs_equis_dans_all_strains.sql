INSERT INTO all_strains
SELECT xxx_id, sch_historique, arr[nr] AS strain, arr[nr] AS short_strain, nr
FROM  (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM  (SELECT xxx_id, sch_historique, string_to_array(sch_references_equi, ';') AS arr FROM t_souche 
		  WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)) t
   ) sub;
