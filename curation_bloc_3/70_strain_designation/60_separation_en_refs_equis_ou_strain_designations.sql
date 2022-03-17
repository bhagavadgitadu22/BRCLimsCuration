DROP TABLE IF EXISTS new_refs_equis;
DROP TABLE IF EXISTS new_strain_designations;

SELECT *
INTO new_refs_equis
FROM all_strains_grouped
WHERE short_strain LIKE ANY(SELECT CONCAT(collection, '%') FROM bilan_collections)
OR short_strain SIMILAR TO '(CARE|CRBIP|CIP|DSM|ATCC|JCM|NCTC)%';

SELECT * 
INTO new_strain_designations
FROM all_strains_grouped
WHERE (xxx_id, short_strain, position) NOT IN (SELECT * FROM new_refs_equis);
