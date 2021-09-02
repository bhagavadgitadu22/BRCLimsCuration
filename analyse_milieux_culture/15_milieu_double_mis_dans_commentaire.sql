SELECT xxx_id, mil_designation_en, mil_commentaire_compo
FROM t_milieu
WHERE mil_clg_id = 401
AND LOWER(mil_commentaire_compo) LIKE '%medium%';
