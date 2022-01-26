DROP TABLE IF EXISTS casser_les_strains;

-- de même avec short_strain qui contiennent encore strain dans leur nom
SELECT xxx_id, sch_historique, arr[nr] AS old_strain, 
btrim((string_to_array(arr[nr], '('))[1], '/) ') AS new_strain, nr
INTO TEMPORARY TABLE casser_les_strains
FROM  (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM  (SELECT xxx_id, sch_historique, string_to_array(short_strain, 'strain') AS arr FROM all_strains
		  WHERE short_strain SIMILAR TO '%strain%') t
   ) sub;

DELETE FROM all_strains
WHERE (xxx_id, short_strain) IN (SELECT xxx_id, old_strain FROM casser_les_strains);

INSERT INTO all_strains
SELECT xxx_id, sch_historique, new_strain, new_strain, nr AS short_strain 
FROM casser_les_strains;

-- on supprime les strains vides (ne comportant ni chiffre ni lettre...)
DELETE FROM all_strains
WHERE short_strain NOT SIMILAR TO '%[a-zA-Z0-9]+%';

UPDATE all_strains
SET short_strain = 'ATCC 27647'
WHERE short_strain = 'ATCC 27647  (souche-type)';

UPDATE all_strains
SET short_strain = 'B 6 «25»'
WHERE short_strain = 'B 6 «25';

UPDATE all_strains
SET short_strain = 'Patoc 1'
WHERE short_strain = 'Patoc 1,Pas de dossier';
