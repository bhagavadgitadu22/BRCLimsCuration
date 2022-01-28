UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int. J. Syst. Evol., Microbiol', 'Int. J. Syst. Evol. Microbiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Int. J. Syst. Evol., Microbiol', 'Int. J. Syst. Evol. Microbiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Microbiol., Immunol', 'Microbiol. Immunol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Microbiol., Immunol', 'Microbiol. Immunol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Microbiol., Biotechno', 'J. Microbiol. Biotechno')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Microbiol., Biotechno', 'J. Microbiol. Biotechno');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Gen., Microbiol', 'J. Gen. Microbiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Gen., Microbiol', 'J. Gen. Microbiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'World J. Microbiol., Biotechnol', 'World J. Microbiol. Biotechnol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'World J. Microbiol., Biotechnol', 'World J. Microbiol. Biotechnol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Am., Chem. Soc', 'J. Am. Chem. Soc')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Am., Chem. Soc', 'J. Am. Chem. Soc');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Genome Biol., Evol', 'Genome Biol. Evol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Genome Biol., Evol', 'Genome Biol. Evol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'FEMS Microbiol., Ecol', 'FEMS Microbiol. Ecol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'FEMS Microbiol., Ecol', 'FEMS Microbiol. Ecol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'FEMS Microbiol., Lett', 'FEMS Microbiol. Lett')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'FEMS Microbiol., Lett', 'FEMS Microbiol. Lett');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int. J. Syst. Evol, Microbiol', 'Int. J. Syst. Evol. Microbiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Int. J. Syst. Evol, Microbiol', 'Int. J. Syst. Evol. Microbiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Path. Microbiol. Scand., Sec. B', 'Acta Path. Microbiol. Scand. Sec. B')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Acta Path. Microbiol. Scand., Sec. B', 'Acta Path. Microbiol. Scand. Sec. B');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Path. Microbiol. Scand., Sec.B', 'Acta Path. Microbiol. Scand. Sec.B')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Acta Path. Microbiol. Scand., Sec.B', 'Acta Path. Microbiol. Scand. Sec.B');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Agric. Biol., Chem', 'Agric. Biol. Chem')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Agric. Biol., Chem', 'Agric. Biol. Chem');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Ann. Microbiol., Inst. Pasteur', 'Ann. Microbiol. Inst. Pasteur')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Ann. Microbiol., Inst. Pasteur', 'Ann. Microbiol. Inst. Pasteur');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Annales Microbiol., Inst. Pasteur', 'Annales Microbiol. Inst. Pasteur')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Annales Microbiol., Inst. Pasteur', 'Annales Microbiol. Inst. Pasteur');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Amer, J. Epidemiol', 'Amer. J. Epidemiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Amer, J. Epidemiol', 'Amer. J. Epidemiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Appl. Microbiol., Biotechnol', 'Appl. Microbiol. Biotechnol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Appl. Microbiol., Biotechnol', 'Appl. Microbiol. Biotechnol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'FEMS, Immunol. Med. Microb', 'FEMS Immunol. Med. Microb')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'FEMS, Immunol. Med. Microb', 'FEMS Immunol. Med. Microb');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'FEMS, Microbiol. Lett', 'FEMS Microbiol. Lett')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'FEMS, Microbiol. Lett', 'FEMS Microbiol. Lett');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Antimicrob., Chemother', 'J. Antimicrob. Chemother')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Antimicrob., Chemother', 'J. Antimicrob. Chemother');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Hyg., Camb', 'J. Hyg. Camb')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Hyg., Camb', 'J. Hyg. Camb');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Clinical, Microbiol', 'J. Clinical. Microbiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Clinical, Microbiol', 'J. Clinical. Microbiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Dairy, Res', 'J. Dairy. Res')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Dairy, Res', 'J. Dairy. Res');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Clinical, Microbiol', 'J. Clinical. Microbiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Clinical, Microbiol', 'J. Clinical. Microbiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J. Microbiol., Methods', 'J. Microbiol. Methods')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'J. Microbiol., Methods', 'J. Microbiol. Methods');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Microbiol., Pathog', 'Microbiol. Pathog')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Microbiol., Pathog', 'Microbiol. Pathog');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Mol. Biol., Evol', 'Mol. Biol. Evol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Mol. Biol., Evol', 'Mol. Biol. Evol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Nature, London', 'Nature London')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Nature, London', 'Nature London');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Syst. Applied, Microbiol', 'Syst. Applied. Microbiol')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Syst. Applied, Microbiol', 'Syst. Applied. Microbiol');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Annales de Microbiol., Inst. Pasteur', 'Annales de Microbiol. Inst. Pasteur')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'Annales de Microbiol., Inst. Pasteur', 'Annales de Microbiol. Inst. Pasteur');

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'C. R. Acad. Sci., Paris', 'C. R. Acad. Sci. Paris')
WHERE xxx_id IN (SELECT xxx_id FROM souches_groupe_cip)
AND sch_bibliographie != REPLACE(sch_bibliographie, 'C. R. Acad. Sci., Paris', 'C. R. Acad. Sci. Paris');
