DROP TABLE IF EXISTS souches_triees;

CREATE TABLE souches_triees (
  id SERIAL,
  sch_identifiant varchar(75)
);

INSERT INTO souches_triees(sch_identifiant)
SELECT sch_identifiant
FROM (SELECT DISTINCT sch_identifiant FROM t_souche) AS a
WHERE trim(sch_identifiant) SIMILAR TO 'CIP A[0-9]+T?'
ORDER BY (REGEXP_MATCHES(sch_identifiant, '[0-9]+'))[1]::int;

INSERT INTO souches_triees(sch_identifiant)
SELECT sch_identifiant
FROM (SELECT DISTINCT sch_identifiant FROM t_souche) AS a
WHERE trim(sch_identifiant) SIMILAR TO 'CIP [0-9]{2}.[0-9]+T?'
ORDER BY sch_identifiant;

INSERT INTO souches_triees(sch_identifiant)
SELECT sch_identifiant
FROM (SELECT DISTINCT sch_identifiant FROM t_souche) AS a
WHERE trim(sch_identifiant) SIMILAR TO 'CIP [0-9]{1}.[0-9]+T?';

INSERT INTO souches_triees(sch_identifiant)
SELECT sch_identifiant
FROM (SELECT DISTINCT sch_identifiant FROM t_souche) AS a
WHERE trim(sch_identifiant) SIMILAR TO 'CIP 1[0-9]{5}T?';

SELECT * FROM souches_triees;
