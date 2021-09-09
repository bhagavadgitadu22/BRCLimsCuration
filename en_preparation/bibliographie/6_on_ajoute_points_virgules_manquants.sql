UPDATE t_souche
SET sch_bibliographie = REPLACE(
	sch_bibliographie, 
	'J. Bacteriol., 1972, 110, 424 Curr. Microbiol., 1984, 10, 221 Int. J. Syst. Bacteriol., 1984, 34, 503', 
	'J. Bacteriol., 1972, 110, 424; Curr. Microbiol., 1984, 10, 221; Int. J. Syst. Bacteriol., 1984, 34, 503'
)
WHERE sch_bibliographie LIKE '%J. Bacteriol., 1972, 110, 424 Curr. Microbiol., 1984, 10, 221 Int. J. Syst. Bacteriol., 1984, 34, 503%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(
	sch_bibliographie, 
	'Int. J. Syst. Evol. Microbiol. 2002, 52: 195-205Int. J. Syst. Evol. Microbiol. 2002, 52: 293-295Int. J. Syst. Evol. Microbiol., 2004, 54, 1773-1788.', 
	'Int. J. Syst. Evol. Microbiol. 2002, 52: 195-205;Int. J. Syst. Evol. Microbiol. 2002, 52: 293-295;Int. J. Syst. Evol. Microbiol., 2004, 54, 1773-1788.'
)
WHERE sch_bibliographie LIKE '%Int. J. Syst. Evol. Microbiol. 2002, 52: 195-205Int. J. Syst. Evol. Microbiol. 2002, 52: 293-295Int. J. Syst. Evol. Microbiol., 2004, 54, 1773-1788.%';

UPDATE t_souche
SET sch_bibliographie = REPLACE(
	sch_bibliographie, 
	'PLoS Negl. Trop. Dis., 2019, May 23, 13(5) :e0007270', 
	'PLoS Negl. Trop. Dis., 2019, 13(5), e0007270'
)
WHERE sch_bibliographie LIKE '%PLoS Negl. Trop. Dis., 2019, May 23, 13(5) :e0007270%';
