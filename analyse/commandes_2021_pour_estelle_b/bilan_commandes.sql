SELECT cmd_num_bon_livraison 
FROM t_commande
WHERE cmd_num_bon_livraison SIMILAR TO '[0-9]+'
ORDER BY cmd_num_bon_livraison::integer DESC