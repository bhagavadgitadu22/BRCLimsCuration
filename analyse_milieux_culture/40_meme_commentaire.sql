SELECT ARRAY_AGG(xxx_id), ARRAY_AGG(mil_designation_en), ref_equi FROM

(SELECT xxx_id, mil_designation_en, REGEXP_MATCHES(mil_commentaire_compo, '[a-zA-Z]+ [0-9]+', 'g') AS ref_equi
FROM t_milieu
WHERE mil_clg_id = 401
AND mil_commentaire_compo != ''
ORDER BY xxx_id) AS a

GROUP BY ref_equi
HAVING COUNT(*) > 1;
