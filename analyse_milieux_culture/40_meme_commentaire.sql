SELECT ref_equi FROM
(SELECT xxx_id, REGEXP_MATCHES(mil_commentaire_compo, '[a-zA-Z]+ [0-9]+', 'g') AS ref_equi
FROM t_milieu
WHERE mil_commentaire_compo != ''
ORDER BY xxx_id) AS a
GROUP BY ref_equi
HAVING COUNT(*) > 1

/*
('ATCC', 'CAIM', 'CCUG', 'DSM', 'NCIMB', 'NCPPB', 'NCTC', 'NRRL', 'VTT', 'CECT', 'NCIMB', 'JCM', 'ATCC', 'IFO', 'LMG', 'ACAM', 'UMIP'
*/
