DELETE FROM t_dico_liste_val
WHERE dlv_att_id IN 
(SELECT xxx_id FROM t_attribut
WHERE att_nom = 'Featured Collections');

DELETE FROM t_attribut
WHERE att_nom = 'Featured Collections';
