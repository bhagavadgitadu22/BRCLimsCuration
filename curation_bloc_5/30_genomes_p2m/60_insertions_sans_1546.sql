INSERT INTO t_carac_phenotypique_resultat (xxx_cre_usr_id, xxx_maj_usr_id, cpr_sch_id, cpr_cpy_id, cpr_com)  
SELECT xxx_cre_usr_id, xxx_maj_usr_id, cpr_sch_id, cpr_cpy_id, str FROM 
(SELECT (SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin') AS xxx_cre_usr_id,
(SELECT xxx_id FROM t_utilisateur WHERE usr_log = 'superadmin') AS xxx_maj_usr_id, 
xxx_id AS cpr_sch_id, (SELECT xxx_id FROM t_carac_phenotypique AS t_cp WHERE t_cp.cpy_numero = 1546) AS cpr_cpy_id,
CONCAT('P2M ', array_to_string(ARRAY_AGG(p2m), ', ')) AS str
FROM souches_sans_infos
GROUP BY xxx_id) AS a
WHERE (length(str) - length(regexp_replace(str, '[0-9]{6}', '', 'g')))/6 = 1;
