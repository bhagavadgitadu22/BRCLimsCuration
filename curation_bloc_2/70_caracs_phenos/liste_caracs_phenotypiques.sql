SELECT cpy_numero, don_lib, cpy_methode
FROM t_carac_phenotypique
JOIN t_donneedico
ON cpy_id = t_donneedico.xxx_id
GROUP BY cpy_numero, don_lib, cpy_methode
ORDER BY cpy_numero;
