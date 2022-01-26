DROP TABLE IF EXISTS casser_les_egaux;

-- on casse certaines strains qui comportent des égal et sont donc plusieurs strains à la fois
UPDATE all_strains
SET short_strain = 'SB3437 (=KpFITDHA-1 = SHV-2)'
WHERE short_strain = 'SB3437 (=KpFITDHA-1 et SHV-2)';

SELECT xxx_id, sch_historique, arr[nr] AS old_strain, 
btrim(regexp_replace(btrim(arr[nr], '() '), 'strain', ''), ' :') AS new_strain, nr
INTO TEMPORARY TABLE casser_les_egaux
FROM  (
   SELECT *, generate_subscripts(arr, 1) AS nr
   FROM  (SELECT xxx_id, sch_historique, string_to_array(short_strain, '=') AS arr FROM all_strains
		  WHERE short_strain SIMILAR TO '%=%'
		  AND short_strain NOT SIMILAR TO '%\) ?\(%') t
   ) sub;
   
DELETE FROM all_strains
WHERE (xxx_id, short_strain) IN (SELECT xxx_id, old_strain FROM casser_les_egaux);

INSERT INTO all_strains
SELECT xxx_id, sch_historique, new_strain, new_strain, nr AS short_strain 
FROM casser_les_egaux;
