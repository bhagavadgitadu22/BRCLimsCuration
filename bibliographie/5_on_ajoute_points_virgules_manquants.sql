UPDATE t_souche
SET sch_bibliographie = REPLACE(
	sch_bibliographie, 
	'J. Bacteriol., 1972, 110, 424 Curr. Microbiol., 1984, 10, 221 Int. J. Syst. Bacteriol., 1984, 34, 503', 
	'J. Bacteriol., 1972, 110, 424; Curr. Microbiol., 1984, 10, 221; Int. J. Syst. Bacteriol., 1984, 34, 503'
)
WHERE sch_bibliographie LIKE '%J. Bacteriol., 1972, 110, 424 Curr. Microbiol., 1984, 10, 221 Int. J. Syst. Bacteriol., 1984, 34, 503%';
