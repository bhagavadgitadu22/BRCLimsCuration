SELECT xxx_id, sch_identifiant, sch_version, sch_isole_a_partir_de 
FROM last_version_souches_cip 
WHERE sch_isole_a_partir_de 
SIMILAR TO '%(DEAN strain|\+ 1\% yeast|Study \+ 0.5\% yeast|Var. aterrimus|Var. halodurans|Var. niger|Bioch. micro. I.P.|2011, Human, urine|1995, Human, blood|1995, Human, Blood)%';
