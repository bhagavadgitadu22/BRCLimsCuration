DROP TABLE IF EXISTS casser_les_egaux;
DROP TABLE IF EXISTS casser_les_strains;

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

-- de même avec short_strain qui contiennent encore strain dans leur nom
SELECT xxx_id, sch_historique, short_strain AS old_strain,
btrim((string_to_array(unnest(string_to_array(short_strain, 'strain')), '('))[1], '/) ') AS new_strain
INTO TEMPORARY TABLE casser_les_strains
FROM all_strains
WHERE short_strain SIMILAR TO '%strain%'
ORDER BY xxx_id;

DELETE FROM all_strains
WHERE (xxx_id, short_strain) IN (SELECT xxx_id, old_strain FROM casser_les_strains);

-- on supprime les strains vides (ne comportant ni chiffre ni lettre...)
DELETE FROM all_strains
WHERE short_strain NOT SIMILAR TO '%[a-zA-Z0-9]+%';
