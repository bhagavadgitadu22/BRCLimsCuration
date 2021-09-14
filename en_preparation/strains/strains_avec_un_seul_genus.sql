SELECT * FROM

(SELECT DISTINCT ON (xxx_id, sch_historique, strain) xxx_id, sch_historique, strain,
true_strain
FROM

(SELECT xxx_id, sch_historique, strain,
CASE WHEN strain_minus_genus = '' THEN btrim(
		REPLACE(REPLACE(REPLACE(REPLACE(
			strain, CHR(127), ''), CHR(9), ''), CHR(13), ''), CHR(10), ''
		), ';. :-,"('
	) 
	ELSE btrim(
		REPLACE(REPLACE(REPLACE(REPLACE(
			strain_minus_genus, CHR(127), ''), CHR(9), ''), CHR(13), ''), CHR(10), ''
		), ';. :-,"('
	)
END AS true_strain FROM
 
(SELECT xxx_id, genus_name, sch_historique, strain, 
(regexp_matches(strain, CONCAT('.*?(?=', genus_name, ')')))[1] AS strain_minus_genus
FROM
 
(SELECT xxx_id, sch_identifiant, sch_references_equi, sch_historique, 
trim((regexp_matches(sch_historique, '(?<=strain).*?(?=<-|->|<|$)', 'g'))[1]) AS strain
FROM t_souche
ORDER BY xxx_id) AS a

LEFT JOIN (SELECT DISTINCT genus_name FROM taxonomy) AS b
ON a.strain LIKE CONCAT('%', b.genus_name, '%')) AS minus_genus

) AS total

ORDER BY xxx_id, sch_historique, strain, char_length(true_strain)) AS rand

ORDER BY random();
