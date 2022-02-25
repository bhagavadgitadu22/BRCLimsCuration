DROP TABLE IF EXISTS max_refs;

SELECT xxx_id,
CASE WHEN sch_references_equi IS NULL OR sch_references_equi = '' THEN 0
ELSE array_length(string_to_array(sch_references_equi, ';'), 1)
END AS nombre_equis_refs
INTO max_refs
FROM t_souche;

UPDATE all_strains
SET number_row = all_strains.number_row+nombre_equis_refs
FROM max_refs
WHERE all_strains.xxx_id = max_refs.xxx_id;

INSERT INTO all_strains
SELECT xxx_id, sch_historique, arr[nr] AS strain, arr[nr] AS short_strain, nr AS number_row
FROM  (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM  (SELECT xxx_id, sch_historique, string_to_array(sch_references_equi, ';') AS arr FROM t_souche 
		  WHERE xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)) t
   ) sub;
