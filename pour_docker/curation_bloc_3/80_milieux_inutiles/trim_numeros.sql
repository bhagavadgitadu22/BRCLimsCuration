UPDATE t_milieu
SET mil_numero = TRIM(mil_numero)
WHERE mil_clg_id = 401
AND mil_numero != TRIM(mil_numero);
