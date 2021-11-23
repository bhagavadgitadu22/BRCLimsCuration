UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Antimicrob', 'J. Antimicrob')
WHERE sch_bibliographie LIKE '%J; Antimicrob%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Clin', 'J. Clin')
WHERE sch_bibliographie LIKE '%J; Clin%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int; J', 'Int. J')
WHERE sch_bibliographie LIKE '%Int; J%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Gen', 'J. Gen')
WHERE sch_bibliographie LIKE '%J; Gen%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Path; Microbiol', 'Acta Path. Microbiol')
WHERE sch_bibliographie LIKE '%Acta Path; Microbiol%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int. J. Syst; Evol', 'Int. J. Syst. Evol')
WHERE sch_bibliographie LIKE '%Int. J. Syst; Evol%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Biotechnol. Appl; Biochem', 'Biotechnol. Appl. Biochem')
WHERE sch_bibliographie LIKE '%Biotechnol. Appl; Biochem%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Actinomycetes, 1977, 12, 30; in "The Actinomycetales. The Jena International Symposium of Taxonomy". H.A. Lechevalier and M.P. Lechevalier. VEB Gustav Fischer Verlag, Jena, 1970, 393', 'Actinomycetes, 1977, 12, 30, in "The Actinomycetales. The Jena International Symposium of Taxonomy". H.A. Lechevalier and M.P. Lechevalier. VEB Gustav Fischer Verlag, Jena, 1970, 393')
WHERE sch_bibliographie LIKE '%Actinomycetes, 1977, 12, 30; in "The Actinomycetales. The Jena International Symposium of Taxonomy". H.A. Lechevalier and M.P. Lechevalier. VEB Gustav Fischer Verlag, Jena, 1970, 393%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Science, 1982, 216, 1317; Int.', 'Science, 1982, 216, 1317;')
WHERE sch_bibliographie LIKE '%Science, 1982, 216, 1317; Int.%';
