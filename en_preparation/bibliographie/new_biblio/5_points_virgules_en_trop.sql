UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Antimicrob', 'J. Antimicrob')
WHERE sch_bibliographie LIKE '%J; Antimicrob%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Clin', 'J. Clin')
WHERE sch_bibliographie LIKE '%J; Clin%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int; J', 'Int. J')
WHERE sch_bibliographie LIKE '%Int; J%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'J; Gen', 'J. Gen')
WHERE sch_bibliographie LIKE '%J; Gen%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Path; Microbiol', 'Acta Path. Microbiol')
WHERE sch_bibliographie LIKE '%Acta Path; Microbiol%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int. J. Syst; Evol', 'Int. J. Syst. Evol')
WHERE sch_bibliographie LIKE '%Int. J. Syst; Evol%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Biotechnol. Appl; Biochem', 'Biotechnol. Appl. Biochem')
WHERE sch_bibliographie LIKE '%Biotechnol. Appl; Biochem%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Actinomycetes, 1977, 12, 30; in "The Actinomycetales. The Jena International Symposium of Taxonomy". H.A. Lechevalier and M.P. Lechevalier. VEB Gustav Fischer Verlag, Jena, 1970, 393', 'Actinomycetes, 1977, 12, 30, in "The Actinomycetales. The Jena International Symposium of Taxonomy". H.A. Lechevalier and M.P. Lechevalier. VEB Gustav Fischer Verlag, Jena, 1970, 393')
WHERE sch_bibliographie LIKE '%Actinomycetes, 1977, 12, 30; in "The Actinomycetales. The Jena International Symposium of Taxonomy". H.A. Lechevalier and M.P. Lechevalier. VEB Gustav Fischer Verlag, Jena, 1970, 393%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Science, 1982, 216, 1317; Int.', 'Science, 1982, 216, 1317;')
WHERE sch_bibliographie LIKE '%Science, 1982, 216, 1317; Int.%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Path. Microbiol. Scand; Sec. B', 'Acta Path. Microbiol. Scand, Sec. B')
WHERE sch_bibliographie LIKE '%Acta Path. Microbiol. Scand; Sec. B%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Proc. Natl; Acad. Sci. USA', 'Proc. Natl. Acad. Sci. USA')
WHERE sch_bibliographie LIKE '%Proc. Natl; Acad. Sci. USA%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, '; ;', ';')
WHERE sch_bibliographie LIKE '%; ;%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Acta Microbiol., Immunol; Hung', 'Acta Microbiol. Immunol. Hung')
WHERE sch_bibliographie LIKE '%Acta Microbiol., Immunol; Hung%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'PLoS One. 2017 Jun 22;12(6):e0179997. doi: 10.1371/journal.pone.0179997. PMID: 28640915; PMCID: PMC5481030;', 'PLoS One, 2017, 12(6), e0179997, doi: 10.1371/journal.pone.0179997, PMID: 28640915, PMCID: PMC5481030;')
WHERE sch_bibliographie LIKE '%PLoS One. 2017 Jun 22;12(6):e0179997. doi: 10.1371/journal.pone.0179997. PMID: 28640915; PMCID: PMC5481030;%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Produces beta-lactamase ; highly gentamicin-resistant isolate Antimicrob. Agents Chemother., 1993, 37, 1447.', 'Antimicrob. Agents Chemother., 1993, 37, 1447.')
WHERE sch_bibliographie LIKE '%Produces beta-lactamase ; highly gentamicin-resistant isolate Antimicrob. Agents Chemother., 1993, 37, 1447.%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Bacteriol. Rev., 1973, 37, 522; 35;', 'Bacteriol. Rev., 1973, 37, 522;')
WHERE sch_bibliographie LIKE '%Bacteriol. Rev., 1973, 37, 522; 35;%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, ';Int. J. Syst. Evol. Microbiol.', 'Int. J. Syst. Evol. Microbiol.')
WHERE sch_bibliographie LIKE '%;Int. J. Syst. Evol. Microbiol.%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Res. Microbiol;', 'Res. Microbiol.')
WHERE sch_bibliographie LIKE '%Res. Microbiol;%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, 'Int. J. Syst. Evol. Microbiol;', 'Int. J. Syst. Evol. Microbiol.')
WHERE sch_bibliographie LIKE '%Int. J. Syst. Evol. Microbiol;%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);

UPDATE t_souche
SET sch_bibliographie = REPLACE(sch_bibliographie, ' WHO Collaborating Centre for Reference and Research on Influenza (04-APR-2007);', 'WHO Collaborating Centre for Reference and Research on Influenza (04-APR-2007);')
WHERE sch_bibliographie LIKE '%WHO Collaborating Centre for Reference and Research on Influenza (04-APR-2007);%'
AND t_souche.xxx_id IN (SELECT xxx_id FROM souches_groupe_cip);
