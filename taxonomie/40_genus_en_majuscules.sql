-- on met en majuscules les genus qui ne le sont pas
UPDATE t_donneedico
SET don_lib = genus_name
FROM taxonomy
WHERE don_dic_id = 3755 AND don_parent = 0
AND LOWER(don_lib) = LOWER(genus_name)
AND don_lib != genus_name;