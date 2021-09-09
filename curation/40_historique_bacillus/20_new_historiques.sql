-- puis enfin on reformatte les mauvais historiques en bons historiques
DROP TABLE IF EXISTS new_historiques;

SELECT a.xxx_id, 
CASE 
	WHEN strain IS NOT NULL	THEN CONCAT(str, ': ', strain)
	ELSE str
END AS new_historique 
INTO new_historiques FROM

(SELECT xxx_id, string_agg(CONCAT(bonne_annee, ', ', texte), ' <- ' ORDER BY numero DESC) AS str
FROM lines_bacillus
WHERE texte != ''
GROUP BY xxx_id) AS a

LEFT JOIN strains_bacillus
ON a.xxx_id = strains_bacillus.xxx_id;

UPDATE t_souche
SET sch_historique = new_historique 
FROM new_historiques
WHERE t_souche.xxx_id = new_historiques.xxx_id;
