DROP TABLE IF EXISTS all_strains;
DROP TABLE IF EXISTS special_taxonomy;

SELECT DISTINCT genus_name 
INTO special_taxonomy
FROM taxonomy
UNION 
VALUES ('Aerobacter'), ('Thermobacterium'), ('Actinobacterium'), ('Lophomonas'), ('Lactobacterium'), 
		('Plectridium'), ('Betabacterium'), ('Bacterium'), ('Salinoactinobacterium'), ('Gardenerella'),
		('Alcaligenaceae'), ('Welchia'), ('Betacoccus'), ('Sciurus'), ('Odontomyces'), 
		('Moxarella'), ('Minibacterium'), ('Proactinomyces'), ('Solicoccus'), ('Enterobacter'),
		('Herellea'), ('Hydrogenomonas'), ('Flavobactrium'), ('Paracolobactrum'), ('Plectridium'), 
		('Paracoli'), ('Streptobacterium'), ('Diplococcus'), ('Propionivacterium'), ('Krusella'),
		('Cocobacillus'), ('Phytomonas'), ('Yeomjeonicoccus'), ('Pseudanabaena'), ('Geitlerinema'),
		('Renobacter'), ('Eidothea'), ('Eurybia'), ('Larus'), ('Jensenia'),
		('Erysipelothrine'), ('Mima'), ('Louisia'), ('Thuringiensis');

SELECT xxx_id, sch_identifiant, sch_references_equi, sch_historique, strain, true_strain, 
ROW_NUMBER () OVER (ORDER BY xxx_id, sch_identifiant, sch_references_equi, sch_historique, strain, true_strain) 
INTO all_strains
FROM

(SELECT DISTINCT ON (xxx_id, sch_identifiant, sch_references_equi, sch_historique, strain) 
xxx_id, sch_identifiant, sch_references_equi, sch_historique, strain,
true_strain
FROM

(SELECT xxx_id, sch_identifiant, sch_references_equi, sch_historique, strain,
CASE WHEN genus_name IS NULL THEN btrim(
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
 
(SELECT xxx_id, genus_name, sch_identifiant, sch_references_equi, sch_historique, strain, 
(regexp_matches(strain, CONCAT('.*?(?=', genus_name, ')')))[1] AS strain_minus_genus
FROM
 
(SELECT xxx_id, sch_identifiant, sch_references_equi, sch_historique, 
trim((regexp_matches(sch_historique, '(?<=strain).*?(?=<-|->|<|$)', 'g'))[1]) AS strain
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
ORDER BY xxx_id) AS a

LEFT JOIN special_taxonomy AS b
ON a.strain LIKE CONCAT('%', b.genus_name, '%')) AS minus_genus

) AS total

ORDER BY xxx_id, sch_identifiant, sch_references_equi, sch_historique, strain, char_length(true_strain)) AS rand

ORDER BY random();
