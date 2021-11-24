UPDATE t_souche
SET sch_bibliographie = E'Press Med., 1949, 57, 1230;\nInt. J. Syst. Bacteriol., 1985, 35, 342.'
WHERE sch_bibliographie = 'Press Med., 1949, 57, 1230;Int. J. Syst. Bacteriol., 1985, 35, 342.'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = regexp_replace(sch_bibliographie, E'Int. J. Syst. Evol. Microbiol., 2016, 66, 4422[\\n\\r]+-4432;', 'Int. J. Syst. Evol. Microbiol., 2016, 66, 4422-4432;', 'g')
WHERE sch_bibliographie SIMILAR TO E'%Int. J. Syst. Evol. Microbiol., 2016, 66, 4422[\\n\\r]+-4432;%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);
