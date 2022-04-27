SELECT t_souche.xxx_id, sch_identifiant,
t_donneedico.don_lib, seq_sequence, seq_blast, 
--seq_qualite, 
seq_lien_base_publique, seq_com, 
array_to_string(ARRAY_AGG(tdd2.don_lib), ', ') AS primers
FROM t_souche
JOIN t_sequence
ON seq_sch_id = t_souche.xxx_id
JOIN t_donneedico
ON seq_type = t_donneedico.xxx_id
LEFT JOIN t_sequenceprimer
ON spr_seq_id = t_sequence.xxx_id
LEFT JOIN t_typesequence_primer
ON spr_tsp_id = t_typesequence_primer.xxx_id
LEFT JOIN t_donneedico AS tdd2
ON tsp_id = tdd2.xxx_id
WHERE t_souche.xxx_id IN (SELECT xxx_id FROM last_version_souches_cip)
AND sch_catalogue IS True
AND sch_mot IS False
GROUP BY t_souche.xxx_id, sch_identifiant, sch_version, t_donneedico.don_lib, 
seq_sequence, seq_blast, seq_lien_base_publique, seq_com
ORDER BY t_souche.xxx_id;