DROP TABLE IF EXISTS new_refs_equis;
DROP TABLE IF EXISTS new_strain_designations;

SELECT * 
INTO new_refs_equis
FROM all_strains
WHERE short_strain LIKE ANY(SELECT CONCAT(collection, '%') FROM bilan_collections);

SELECT * 
INTO new_strain_designations
FROM all_strains
WHERE short_strain NOT LIKE ANY(SELECT CONCAT(collection, '%') FROM bilan_collections);
