SELECT cmp_designation_en, ARRAY_AGG(cmp_fournisseur), ARRAY_AGG(cmp_com), COUNT(*)
FROM t_composition
GROUP BY cmp_designation_en
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;
