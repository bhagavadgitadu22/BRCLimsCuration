DROP TABLE IF EXISTS ids_serovar;
DROP TABLE IF EXISTS parents_serovar;

-- d'abord on récupère la liste des ids de serovar et les ids parents
WITH RECURSIVE children (xxx_id, don_lib, level, don_code, name_path, id_path) AS (
	SELECT
		xxx_id, don_lib, 0, don_code, ARRAY[don_lib::text], ARRAY[xxx_id::integer]
	FROM
		t_donneedico
	WHERE
		don_dic_id = 3755
		AND xxx_sup_dat IS NULL
		AND don_parent = 0
	UNION
		(SELECT
			tdd.xxx_id, tdd.don_lib, t0.level + 1, tdd.don_code, 
		 	ARRAY_APPEND(t0.name_path, tdd.don_lib::text), ARRAY_APPEND(t0.id_path, tdd.xxx_id::integer)
		FROM
			t_donneedico tdd
		INNER JOIN children t0 ON t0.don_code = tdd.don_parent
		WHERE tdd.don_dic_id = 3755 AND tdd.xxx_sup_dat IS NULL)
) SELECT xxx_id AS id_serovar, id_path[2] AS id_parent
INTO TEMPORARY TABLE ids_serovar
FROM children
WHERE level = 2 
AND (name_path[1], name_path[2]) IN (SELECT genus_name, sp_epithet FROM taxonomy WHERE genus_name IS NOT NULL AND sp_epithet IS NOT NULL)
AND (name_path[1], name_path[2], name_path[3]) NOT IN (SELECT genus_name, sp_epithet, subsp_epithet FROM taxonomy WHERE genus_name IS NOT NULL AND sp_epithet IS NOT NULL AND subsp_epithet IS NOT NULL)
AND (name_path[1], name_path[2]) IN (('Bacillus', 'sphaericus'), ('Bacillus', 'thuringiensis'));

/* on récupère le don_code des id_serovar et des id_parent */
SELECT tdd1.don_code AS old_don_parent, tdd2.don_code AS new_don_parent
INTO parents_serovar
FROM t_donneedico AS tdd1, t_donneedico AS tdd2
WHERE (tdd1.xxx_id, tdd2.xxx_id) IN (SELECT id_serovar, id_parent FROM ids_serovar);

-- et on associe les enfants des serovars à leurs parents
UPDATE t_donneedico
SET don_parent = new_don_parent
FROM parents_serovar
WHERE don_parent = old_don_parent
AND t_donneedico.xxx_sup_dat IS NULL;

-- puis on redirige les souches des serovars vers les parents
UPDATE t_souche
SET sch_taxonomie = id_parent
FROM ids_serovar
WHERE sch_taxonomie = id_serovar
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

-- puis on supprime les serovar
UPDATE t_donneedico
SET xxx_sup_dat = now()::timestamp,
	xxx_sup_usr_id = 1
WHERE xxx_id IN (SELECT id_serovar FROM ids_serovar WHERE id_serovar IS NOT NULL);

DROP TABLE IF EXISTS ids_serovar;
DROP TABLE IF EXISTS parents_serovar;
