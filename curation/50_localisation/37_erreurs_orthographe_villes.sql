UPDATE t_donneedico
SET don_lib = 'Tangier'
WHERE don_lib = 'Tanger'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Freiburg im Breisgau'
WHERE don_lib = 'Freiburg'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Krakow'
WHERE don_lib = 'Cracow'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Cape Town'
WHERE don_lib = 'Capetown'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Brussels'
WHERE don_lib = 'Bruxelles'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Geneva'
WHERE don_lib = 'Genève'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Vienna'
WHERE don_lib = 'Wien'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'New York'
WHERE don_lib = 'Nex York'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Tel Aviv-Yafo'
WHERE don_lib = 'Tel aviv'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Mansoura, Egypt'
WHERE don_lib = 'Mansoura'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Guadeloupe'
WHERE don_lib = 'French/Guadeloupe'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Sevilla, Spain'
WHERE don_lib = 'Sevilla, Southern Spain'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Santander, Spain'
WHERE don_lib = 'Santander, Northern Spain'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Nouméa, New Caledonia'
WHERE don_lib = 'New Caledonia/Nouméa'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Ecole Veterinaire de Maisons-Alfort, France'
WHERE don_lib = 'Ecole Veterinaire,(M.Alfort,F'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Papua New Guinea'
WHERE don_lib = 'Papua, New Guinea'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Mogadishu, Somalia'
WHERE don_lib = 'Mogadiscio'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Saint-Nazaire, France'
WHERE don_lib = 'St-nazaire'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Cayenne, French Guiana'
WHERE don_lib = 'French Guiana Française, Cayenne'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Maisons-Alfort, France'
WHERE don_lib = 'Maison-alfort'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Saint-Lô, France'
WHERE don_lib = 'Saint lo'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = CONCAT(don_lib, ', France')
WHERE don_lib IN ('Argentan', 'Pontarlier', 'Calvados', 'Briançon', 'Cahors')
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Venlo, Netherlands'
WHERE don_lib = 'Venlo'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Louvain, Belgium'
WHERE don_lib = 'Louvain'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Fort-de-France, Martinique'
WHERE don_lib = 'Fort-de-France. Martinique'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Tunis, Tunisia'
WHERE don_lib = '(Tunis)'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Beirut, Lebanon'
WHERE don_lib = 'Beyrouth'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Mentakab, Malaysia'
WHERE don_lib = 'Mentekab, Malaya'
AND don_dic_id IN (3758);

UPDATE t_donneedico
SET don_lib = 'Easter Island, Chile'
WHERE don_lib = 'Easter Island'
AND don_dic_id IN (3758);
