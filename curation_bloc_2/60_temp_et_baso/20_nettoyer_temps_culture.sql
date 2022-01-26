UPDATE t_souche
SET sch_temps_culture = REGEXP_REPLACE(sch_temps_culture, '(Juors|J ours|jr|Jour|D D|DAYS)', 'D')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != REGEXP_REPLACE(sch_temps_culture, '(Juors|J ours|jr|Jour|D D|DAYS)', 'D');

UPDATE t_souche
SET sch_temps_culture = REGEXP_REPLACE(sch_temps_culture, 'h.?', 'H')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != REGEXP_REPLACE(sch_temps_culture, 'h.?', 'H');

UPDATE t_souche
SET sch_temps_culture = REGEXP_REPLACE(sch_temps_culture, '(mois|MOIS)', 'M')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != REGEXP_REPLACE(sch_temps_culture, '(mois|MOIS)', 'M');

UPDATE t_souche
SET sch_temps_culture = REGEXP_REPLACE(sch_temps_culture, '(semaines|SEM.|Sem|Semaines|SEM|SEMAINE|S)', 'W')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != REGEXP_REPLACE(sch_temps_culture, '(semaines|SEM.|Sem|Semaines|SEM|SEMAINE|S)', 'W');

UPDATE t_souche
SET sch_temps_culture = btrim(sch_temps_culture, ' ')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != btrim(sch_temps_culture, ' ');

UPDATE t_souche
SET sch_temps_culture = REGEXP_REPLACE(sch_temps_culture, '( | -| -  ?|- |à|, | ?/ ?| ?H ?-? ?|_| D-?){1}(?=[0-9]+)', '-')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != REGEXP_REPLACE(sch_temps_culture, '( | -| -  ?|- |à|, | ?/ ?| ?H ?-? ?|_| D-?){1}(?=[0-9]+)', '-');

UPDATE t_souche
SET sch_temps_culture = REGEXP_REPLACE(sch_temps_culture, '[ ]*(?=[a-zA-Z]+$)', ' ')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture != REGEXP_REPLACE(sch_temps_culture, '[ ]*(?=[a-zA-Z]+$)', ' ');

UPDATE t_souche
SET sch_temps_culture = CONCAT(sch_temps_culture, ' H')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture SIMILAR TO '(18|18-24|24|24-48)';

UPDATE t_souche
SET sch_temps_culture = '24-48 H'
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture = '24-4 8 H';

UPDATE t_souche
SET sch_temps_culture = '3 D'
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_temps_culture = '3 - D';
