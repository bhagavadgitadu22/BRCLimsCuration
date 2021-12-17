DROP TABLE IF EXISTS all_strains;
DROP TABLE IF EXISTS casser_les_egaux;

-- sélection générale des strains des historiques
SELECT DISTINCT xxx_id, sch_historique, 
(regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1] AS strain, 
btrim(regexp_replace((regexp_matches(sch_historique, 'strain.*?(?=<-|->|$)', 'g'))[1], 'strain', ''), ' :') AS short_strain
INTO all_strains
FROM t_souche
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
ORDER BY xxx_id;

-- on casse certaines strains qui comportent des égal et sont donc plusieurs strains à la fois
UPDATE all_strains
SET short_strain = 'SB3437 (=KpFITDHA-1 = SHV-2)'
WHERE short_strain = 'SB3437 (=KpFITDHA-1 et SHV-2)';

SELECT xxx_id, sch_historique, short_strain AS old_strain,
btrim(unnest(string_to_array(short_strain, '=')), '() ') AS new_strain
INTO TEMPORARY TABLE casser_les_egaux
FROM all_strains
WHERE short_strain SIMILAR TO '%=%'
AND short_strain NOT SIMILAR TO '%\) ?\(%'
ORDER BY xxx_id;

DELETE FROM all_strains
WHERE (xxx_id, short_strain) IN (SELECT xxx_id, old_strain FROM casser_les_egaux);

INSERT INTO all_strains
SELECT xxx_id, sch_historique, new_strain, btrim(regexp_replace(new_strain, 'strain', ''), ' :') AS short_strain 
FROM casser_les_egaux;

-- on supprime les strains vides (ne comportent ni chiffre ni lettre...)
DELETE FROM all_strains
WHERE short_strain NOT SIMILAR TO '%[a-zA-Z0-9]+%';
